Summary:	GNU Source Highlight
Summary(pl):	Pod¶wietlanie sk³adni z projektu GNU
Name:		source-highlight
Version:	1.6.3rc
Release:	1
License:	GPL
Group:		Applications/Publishing
Source0:	ftp://ftp.gnu.org/gnu/source-highlight/%{name}-%{version}.tar.gz
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program, given a source file, produces a document with syntax
highlighting.

At the moment this package can handle:

   * Java,
   * C/C++,
   * Prolog,
   * Perl,
   * PHP3 new

as source languages, and HTML as output format.

%description -l pl
Ten program z pliku ¼ród³owego tworzy dokument z pod¶wietlon±
sk³adni±. Aktualnie obs³ugiwane jêzyki ¼ród³owe to Java, C/C++, Prolog
i Perl; wynik jest w HTML.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO.txt doc/*.css
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
%{_datadir}/source-highlight/*.j2h

Summary:	GNU Source Highlight
Summary(pl):	GNU Source Highlight
Name:		source-highlight
Version:	1.3
Release:	1
License:	GPL
Group:		Applications/Publishing
Source0:	ftp://ftp.gnu.org/gnu/source-highlight/%{name}-%{version}.tar.gz
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program, given a source file, produces a document with syntax
highlighting.

At the moment this package can handle

   * Java,
   * C/C++,
   * Prolog, new
   * Perl new

as source languages, and HTML as output format.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog NEWS README THANKS TODO.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.css
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1.gz
%{_datadir}/source-highlight/*.j2h
Summary:	GNU Source Highlight
Summary(pl):	Pod¶wietlanie sk³adni z projektu GNU
Name:		source-highlight
Version:	1.11
Release:	1
License:	GPL
Group:		Applications/Publishing
Source0:	ftp://ftp.gnu.org/gnu/src-highlite/%{name}-%{version}.tar.gz
# Source0-md5:	4d044e7fb4593e9214f64bedad42ea09
URL:		http://www.gnu.org/software/src-highlite/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program, given a source file, produces a document with syntax
highlighting.

At the moment this package can handle:

- Java
- Javascript
- C/C++
- Prolog
- Perl
- Php3
- Python
- Flex
- ChangeLog
- Ruby
- Lua
- Caml
- Sml
- Log

as source languages, and

- HTML
- XHTML
- ANSI color escape sequences (you can use this feature with less)

as output formats.

%description -l pl
Ten program z pliku ¼ród³owego tworzy dokument z pod¶wietlon±
sk³adni±.

Aktualnie obs³ugiwane jêzyki ¼ród³owe to:

- Java
- Javascript
- C/C++
- Prolog
- Perl
- Php3
- Python
- Flex
- ChangeLog
- Ruby
- Lua
- Caml
- Sml
- Log

a wynikiem mo¿e byæ:

- HTML
- XHTML
- kolorowa sekwencja ANSI

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	 DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO.txt doc/*.css
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.j2h

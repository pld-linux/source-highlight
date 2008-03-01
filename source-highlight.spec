Summary:	GNU Source Highlight
Summary(pl.UTF-8):	Podświetlanie składni z projektu GNU
Name:		source-highlight
Version:	2.9
Release:	1
License:	GPL v3+
Group:		Applications/Publishing
Source0:	http://ftp.gnu.org/gnu/src-highlite/%{name}-%{version}.tar.gz
# Source0-md5:	80a947681d32b0fe515a5cd01f9582a7
Patch0:		%{name}-info.patch
URL:		http://www.gnu.org/software/src-highlite/
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	boost-regex-devel
BuildRequires:	flex
BuildRequires:	libstdc++-devel
BuildRequires:	texinfo
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

%description -l pl.UTF-8
Ten program z pliku źródłowego tworzy dokument z podświetloną
składnią.

Aktualnie obsługiwane języki źródłowe to:

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

a wynikiem może być:

- HTML
- XHTML
- kolorowa sekwencja ANSI

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_docdir}/%{name}/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO.txt doc/{*.css,*.html,*.java}
%attr(755,root,root) %{_bindir}/check-regexp
%attr(755,root,root) %{_bindir}/cpp2html
%attr(755,root,root) %{_bindir}/java2html
%attr(755,root,root) %{_bindir}/source-highlight
%attr(755,root,root) %{_bindir}/src-hilite-lesspipe.sh
%{_mandir}/man1/source-highlight.1*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_infodir}/source-highlight.info*

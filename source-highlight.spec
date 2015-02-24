Summary:	GNU Source Highlight
Summary(pl.UTF-8):	Podświetlanie składni z projektu GNU
Name:		source-highlight
Version:	3.1.7
Release:	9
License:	GPL v3+
Group:		Applications/Publishing
Source0:	http://ftp.gnu.org/gnu/src-highlite/%{name}-%{version}.tar.gz
# Source0-md5:	0ff81588d3536b4c4e571122ba940595
Patch0:		%{name}-info.patch
URL:		http://www.gnu.org/software/src-highlite/
BuildRequires:	automake
BuildRequires:	boost-devel >= 1.36.0
BuildRequires:	flex
BuildRequires:	libstdc++-devel
BuildRequires:	texinfo
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program, given a source file, produces a document with syntax
highlighting.

At the moment this package can handle:

- Ada
- Asm (new)
- Applescript (new)
- Awk (new)
- Autoconf files
- Bat (new)
- Bib
- Bison
- C/C++
- C#
- Clipper (new)
- Cobol (new)
- Configuration files (generic)
- Caml
- Changelog
- Css
- D (new)
- Diff
- Erlang (new)
- errors (compiler output) (new)
- Flex
- Fortran
- GLSL
- Haskell
- Haxe
- Html
- ini files
- Java
- Javascript
- KDE desktop files
- Latex
- Ldap files
- Logtalk
- Log files
- lsm files (Linux Software Map)
- Lua
- Makefile
- Manifest (new)
- M4
- ML
- Oz
- Pascal
- Perl
- pkg-config files
- PHP
- Postscript
- Prolog
- Properties files
- Python
- RPM Spec files
- Ruby
- Scala
- Shell
- S-Lang
- Sql
- Tcl
- Texinfo
- VBscript (new)
- XML
- XOrg conf files

as source languages, and

- HTML
- XHTML
- ANSI color escape sequences
- LaTeX
- Texinfo
- DocBook


as output formats.

%description -l pl.UTF-8
Ten program z pliku źródłowego tworzy dokument z podświetloną
składnią.

Aktualnie obsługiwane języki źródłowe to:

- Ada
- Asm (nowość)
- Applescript (nowość)
- Awk (nowość)
- Autoconf files
- Bat (nowość)
- Bib
- Bison
- C/C++
- C#
- Clipper (nowość)
- Cobol (nowość)
- Configuration files (generic)
- Caml
- Changelog
- Css
- D (nowość)
- Diff
- Erlang (nowość)
- errors (compiler output) (nowość)
- Flex
- Fortran
- GLSL
- Haskell
- Haxe
- Html
- ini files
- Java
- Javascript
- KDE desktop files
- Latex
- Ldap files
- Logtalk
- Log files
- lsm files (Linux Software Map)
- Lua
- Makefile
- Manifest (nowość)
- M4
- ML
- Oz
- Pascal
- Perl
- pkg-config files
- PHP
- Postscript
- Prolog
- Properties files
- Python
- RPM Spec files
- Ruby
- Scala
- Shell
- S-Lang
- Sql
- Tcl
- Texinfo
- VBscript (nowość)
- XML
- XOrg conf files

a wynikiem może być:

- HTML
- XHTML
- ANSI color escape sequences
- LaTeX
- Texinfo
- DocBook

%package libs
Summary:	Source highlight library
Summary(pl.UTF-8):	Biblioteka podświetlania składni
Group:		Libraries

%description libs
Source highlight library.

%description libs -l pl.UTF-8
Biblioteka podświetlania składni.

%package devel
Summary:	Header file for srchlite library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki srchlite
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	boost-devel >= 1.36.0
Requires:	libstdc++-devel

%description devel
Header file for srchlite library.

%description devel -l pl.UTF-8
Plik nagłówkowy biblioteki srchlite.

%package static
Summary:	Static source-highlight library
Summary(pl.UTF-8):	Statyczna biblioteka source-highlight
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Statoic source highlight library.

%description static -l pl.UTF-8
Statyczna biblioteka podświetlania składni.

%package -n bash-completion-source-highlight
Summary:	bash-completion for source-higlight
Summary(pl.UTF-8):	bashowe uzupełnianie nazw dla pakietu source-highlight
Group:		Applications/Shells
Requires:	bash-completion

%description -n bash-completion-source-highlight
This package provides bash-completion for source-highlight.

%description -n bash-completion-source-highlight -l pl.UTF-8
Pakiet ten dostarcza bashowe uzupełnianie nazw dla pakiet
source-highlight.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub .
%configure \
	--with-boost-libdir=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -rf docdir-%{name}-%{version}
%{__mv} -f $RPM_BUILD_ROOT%{_docdir}/%{name} docdir-%{name}-%{version}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libsource-highlight.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO.txt doc/{*.css,*.html,*.java}
%doc docdir-%{name}-%{version}/*
%attr(755,root,root) %{_bindir}/check-regexp
%attr(755,root,root) %{_bindir}/cpp2html
%attr(755,root,root) %{_bindir}/java2html
%attr(755,root,root) %{_bindir}/source-highlight
%attr(755,root,root) %{_bindir}/source-highlight-esc.sh
%attr(755,root,root) %{_bindir}/source-highlight-settings
%attr(755,root,root) %{_bindir}/src-hilite-lesspipe.sh
%{_mandir}/man1/check-regexp.1*
%{_mandir}/man1/source-highlight.1*
%{_mandir}/man1/source-highlight-settings.1*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_infodir}/source-highlight.info*
%{_infodir}/source-highlight-lib.info*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsource-highlight.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsource-highlight.so.4

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsource-highlight.so
%{_includedir}/srchilite
%{_pkgconfigdir}/source-highlight.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libsource-highlight.a

%files -n bash-completion-source-highlight
%defattr(644,root,root,755)
%{_sysconfdir}/bash_completion.d/source-highlight

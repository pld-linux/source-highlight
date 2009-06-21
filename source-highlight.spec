Summary:	GNU Source Highlight
Summary(pl.UTF-8):	Podświetlanie składni z projektu GNU
Name:		source-highlight
Version:	2.11.1
Release:	4
License:	GPL v3+
Group:		Applications/Publishing
Source0:	http://ftp.gnu.org/gnu/src-highlite/%{name}-%{version}.tar.gz
# Source0-md5:	f6e332317413f247ce248c52df0ddade
Patch0:		%{name}-info.patch
Patch1:		%{name}-am.patch
URL:		http://www.gnu.org/software/src-highlite/
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	boost-devel >= 1.36.0
BuildRequires:	flex
BuildRequires:	libstdc++-devel
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program, given a source file, produces a document with syntax
highlighting.

At the moment this package can handle:

- Ada (new)
- Autoconf files
- C/C++
- C#
- Bib
- Bison
- Caml
- Changelog
- Css
- Diff
- Flex
- Fortran
- GLSL
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
- M4
- ML
- Pascal
- Perl
- PHP
- Postscript
- Prolog
- Properties files
- Python
- RPM Spec files
- Ruby
- Scala     (new)
- Shell
- S-Lang
- Sql
- Tcl
- XML
- XOrg conf files     (new)

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

- Ada (nowość)
- Autoconf files
- C/C++
- C#
- Bib
- Bison
- Caml
- Changelog
- Css
- Diff
- Flex
- Fortran
- GLSL
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
- M4
- ML
- Pascal
- Perl
- PHP
- Postscript
- Prolog
- Properties files
- Python
- RPM Spec files
- Ruby
- Scala     (nowość)
- Shell
- S-Lang
- Sql
- Tcl
- XML
- XOrg conf files     (nowość)

a wynikiem może być:

- HTML
- XHTML
- ANSI color escape sequences
- LaTeX
- Texinfo
- DocBook

%package -n bash-completion-source-highlight
Summary:	bash-completion for source-higlight
Summary(pl.UTF-8):	bashowe uzupełnianie nazw dla pakietu source-highlight
Group:		Applications/Shells
Requires:	bash-completion

%description -n bash-completion-source-highlight
This package provides bash-completion for source-highlight.

%description -n bash-completion-source-highlight -l pl.UTF-8
Pakiet ten dostarcza bashowe uzupełnianie nazw dla pakiet source-highlight.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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
%{_mandir}/man1/check-regexp.1*
%{_mandir}/man1/source-highlight.1*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_infodir}/source-highlight.info*

%files -n bash-completion-source-highlight
%defattr(644,root,root,755)
%{_sysconfdir}/bash_completion.d/*

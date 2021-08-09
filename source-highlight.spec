Summary:	GNU Source Highlight
Summary(pl.UTF-8):	Podświetlanie składni z projektu GNU
Name:		source-highlight
Version:	3.1.9
Release:	2
License:	GPL v3+
Group:		Applications/Publishing
Source0:	https://ftp.gnu.org/gnu/src-highlite/%{name}-%{version}.tar.gz
# Source0-md5:	a51266164a537c97860d5d9664614dec
Patch0:		%{name}-info.patch
URL:		http://www.gnu.org/software/src-highlite/
BuildRequires:	bison
BuildRequires:	boost-devel >= 1.36.0
BuildRequires:	flex
BuildRequires:	help2man
BuildRequires:	libstdc++-devel
BuildRequires:	texinfo
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program, given a source file, produces a document with syntax
highlighting.

This package can handle many programming languages, e.g. C/C++, Flex,
Java, PHP, Perl, Prolog, Python as source languages; and some output
formats, e.g. HTML, XHTML, LaTeX.

%description -l pl.UTF-8
Ten program z pliku źródłowego tworzy dokument z podświetloną
składnią.

Pakiet potrafi obsłużyć wiele języków programowania, np. C/C++, Flex,
Java, PHP, Perl, Prolog, Python jako języki źródłowe; oraz kilka
formatów wyjściowych, np. HTML, XHTML, LaTeX.

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
export CXXFLAGS="%{rpmcxxflags} -std=c++14"
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

%post	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

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
%{_datadir}/%{name}
%{_infodir}/source-highlight.info*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsource-highlight.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsource-highlight.so.4

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsource-highlight.so
%{_includedir}/srchilite
%{_pkgconfigdir}/source-highlight.pc
%{_infodir}/source-highlight-lib.info*

%files static
%defattr(644,root,root,755)
%{_libdir}/libsource-highlight.a

%files -n bash-completion-source-highlight
%defattr(644,root,root,755)
%{_sysconfdir}/bash_completion.d/source-highlight

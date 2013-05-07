Summary:	Utility library for the Xfce desktop environment
Name:		libxfce4util
Version:	4.10.1
Release:	1
License:	BSD, LGPL
Group:		Libraries
Source0:	http://archive.xfce.org/src/xfce/libxfce4util/4.10/%{name}-%{version}.tar.bz2
# Source0-md5:	11eec87e8eda2bc62512c2416cb807a1
URL:		http://www.xfce.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib-devel
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xfce4-dev-tools >= 4.10.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Basic utility non-GUI functions for Xfce.

%package apidocs
Summary:	libxfce4util API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libxfce4util API documentation.

%package devel
Summary:	Development files for libxfce4util library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xfce4-dev-tools >= 4.10.0

%description devel
Development files for the libxfce4util library.

%package tools
Summary:	Tools for libxfce4util library
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description tools
Tools for libxfce4util library.

%prep
%setup -q

%build
%{__libtoolize}
%{__gtkdocize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/xfce4/help
install -d $RPM_BUILD_ROOT%{_libdir}/xfce4
install -d $RPM_BUILD_ROOT%{_sysconfdir}/xdg/xfce4

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{tl_PH,ur_PK}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING README NEWS THANKS TODO
%attr(755,root,root) %ghost %{_libdir}/libxfce4util.so.?
%attr(755,root,root) %{_libdir}/libxfce4util.so.*.*.*

# commmon dirs
%dir %{_datadir}/xfce4
%{_datadir}/xfce4/help
%{_libdir}/xfce4
%{_sysconfdir}/xdg/xfce4

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxfce4util.so
%dir %{_includedir}/xfce4
%{_includedir}/xfce4/libxfce4util
%{_pkgconfigdir}/*.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/xfce4-kiosk-query


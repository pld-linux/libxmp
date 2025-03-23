#
# Conditional build:
%bcond_without	static_libs	# static library
#
Summary:	Extended Module Player library
Summary(pl.UTF-8):	Biblioteka XMP (Extended Module Player)
Name:		libxmp
Version:	4.6.2
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://downloads.sourceforge.net/xmp/%{name}-%{version}.tar.gz
# Source0-md5:	522c68630de6c3cae696225773621c5c
URL:		https://xmp.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libxmp is a library that renders module files to PCM data. It supports
over 90 mainstream and obscure module formats including Protracker
(MOD), Scream Tracker 3 (S3M), Fast Tracker II (XM), and Impulse
Tracker (IT).

%description -l pl.UTF-8
Libxmp to biblioteka przetwarzająca pliki modułów dźwiękowych na dane
PCM. Obsługuje ponad 90 głównych i mniej znanych formatów, w tym:
Protracker (MOD), Scream Tracker 3 (S3M), Fast Tracker II (XM) oraz
Impulse Tracker (IT).

%package devel
Summary:	Header files for XMP library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki XMP
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for XMP library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki XMP.

%package static
Summary:	Static XMP library
Summary(pl.UTF-8):	Statyczna biblioteka XMP
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static XMP library.

%description static -l pl.UTF-8
Statyczna biblioteka XMP.

%prep
%setup -q

%build
%configure \
	%{?with_static_libs:--enable-static}
%{__make} \
	V=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# omitted from install target
%{__make} install-docs \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL_DATA="cp -p"

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README docs/{CREDITS,Changelog,fixloop.txt,formats.txt}
%attr(755,root,root) %{_libdir}/libxmp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxmp.so.4

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxmp.so
%{_includedir}/xmp.h
%{_pkgconfigdir}/libxmp.pc
%{_libdir}/cmake/libxmp
%{_mandir}/man3/libxmp.3*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libxmp.a
%endif

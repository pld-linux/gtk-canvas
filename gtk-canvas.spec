Summary:	GtkCanvas widget - Tk-like canvas widget for Gtk+
Summary(pl):	GtkCanvas - widget canvas w stylu Tk dla Gtk+
Name:		gtk-canvas
Version:	0.1.1
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	http://www.atai.org/gtk-canvas/%{name}-%{version}.tar.gz
# Source0-md5:	6872220119a4a3c284fe54a186e2ed57
Patch0:		%{name}-nolibs.patch
Patch1:		%{name}-libart_lgpl2.patch
URL:		http://www.atai.org/gtk-canvas/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	imlib-devel >= 1.9
BuildRequires:	libart_lgpl-devel >= 2.3
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libungif-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a straight port of the GNOME Canvas from the stable gnome-libs
1.2.4 back to gtk+ 1.2. The widget is called GtkCanvas.

%description -l pl
Ten pakiet jest bezpo¶rednim portem widgetu GNOME Canvas ze stabilnego
pakietu gnome-libs 1.2.4 z powrotem do gtk+ 1.2. Widget nazywa siê
GtkCanvas.

%package devel
Summary:	Header files for gtk-canvas library
Summary(pl):	Pliki nag³ówkowe biblioteki gtk-canvas
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for gtk-canvas library.

%description devel -l pl
Pliki nag³ówkowe biblioteki gtk-canvas.

%package static
Summary:	Static gtk-canvas library
Summary(pl):	Statyczna biblioteka gtk-canvas
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static gtk-canvas library.

%description static -l pl
Statyczna biblioteka gtk-canvas.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

# GTK_X_CHECKS
tail +1307 acinclude.m4 | head -55 > acinclude.m4.tmp
mv -f acinclude.m4.tmp acinclude.m4

# avoid including these (use system libart_lgpl2)
rm -rf libart_lgpl

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/gtk-canvas.h
%{_includedir}/gtk-canvas

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

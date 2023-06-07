Summary:	Guile-OpenGL - OpenGL interface for GNU Guile
Summary(pl.UTF-8):	Guile-OpenGL - interfejs OpenGL dla GNU Guile
Name:		guile-opengl
Version:	0.2.0
Release:	1
License:	LGPL v3+
Group:		Libraries
Source0:	https://ftp.gnu.org/gnu/guile-opengl/%{name}-%{version}.tar.gz
# Source0-md5:	67c73b8a23fa0be23e8497e6259c794b
Patch0:		%{name}-info.patch
URL:		http://www.gnu.org/software/guile-opengl/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.11
BuildRequires:	guile-devel >= 5:2.0
BuildRequires:	rpmbuild(macros) >= 1.721
BuildRequires:	texinfo
Requires:	guile >= 5:2.0
%if 0%{?_soname_prov:1}
Requires:	%{_soname_prov libGL.so.1}
Suggests:	%{_soname_prov libGLU.so.1}
Suggests:	%{_soname_prov libglut.so.3}
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_debugsource_packages	0

%description
GNU Guile-OpenGL is an OpenGL interface for GNU Guile.

%description -l pl.UTF-8
GNU Guile-OpenGL to interfejs OpenGL dla GNU Guile.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE NEWS README TODO
%{_libdir}/guile/*.*/site-ccache/gl
%{_libdir}/guile/*.*/site-ccache/glu
%{_libdir}/guile/*.*/site-ccache/glut
%{_libdir}/guile/*.*/site-ccache/glx
%{_libdir}/guile/*.*/site-ccache/gl.go
%{_libdir}/guile/*.*/site-ccache/glu.go
%{_libdir}/guile/*.*/site-ccache/glut.go
%{_libdir}/guile/*.*/site-ccache/glx.go
%{_datadir}/guile/site/*.*/gl
%{_datadir}/guile/site/*.*/glu
%{_datadir}/guile/site/*.*/glut
%{_datadir}/guile/site/*.*/glx
%{_datadir}/guile/site/*.*/gl.scm
%{_datadir}/guile/site/*.*/glu.scm
%{_datadir}/guile/site/*.*/glut.scm
%{_datadir}/guile/site/*.*/glx.scm
%{_infodir}/guile-opengl.info*

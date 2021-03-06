Summary:	Guile-OpenGL - OpenGL interface for GNU Guile
Summary(pl.UTF-8):	Guile-OpenGL - interfejs OpenGL dla GNU Guile
Name:		guile-opengl
Version:	0.1.0
Release:	2
License:	LGPL v3+
Group:		Libraries
Source0:	http://ftp.gnu.org/gnu/guile-opengl/%{name}-%{version}.tar.gz
# Source0-md5:	a5d20170103514a042bb13d28f586472
Patch0:		%{name}-info.patch
URL:		http://www.gnu.org/software/guile-opengl/
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

%description
GNU Guile-OpenGL is an OpenGL interface for GNU Guile.

%description -l pl.UTF-8
GNU Guile-OpenGL to interfejs OpenGL dla GNU Guile.

%prep
%setup -q
%patch0 -p1

%build
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
%{_libdir}/guile/2.2/ccache/gl
%{_libdir}/guile/2.2/ccache/glu
%{_libdir}/guile/2.2/ccache/glut
%{_libdir}/guile/2.2/ccache/glx
%{_libdir}/guile/2.2/ccache/gl.go
%{_libdir}/guile/2.2/ccache/glu.go
%{_libdir}/guile/2.2/ccache/glut.go
%{_libdir}/guile/2.2/ccache/glx.go
%{_datadir}/guile/site/2.2/gl
%{_datadir}/guile/site/2.2/glu
%{_datadir}/guile/site/2.2/glut
%{_datadir}/guile/site/2.2/glx
%{_datadir}/guile/site/2.2/gl.scm
%{_datadir}/guile/site/2.2/glu.scm
%{_datadir}/guile/site/2.2/glut.scm
%{_datadir}/guile/site/2.2/glx.scm
%{_infodir}/guile-opengl.info*

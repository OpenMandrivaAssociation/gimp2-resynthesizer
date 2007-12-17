%define plugin_name	resynthesizer
%define version 0.15
%define release %mkrel 1
%define name	gimp2-%plugin_name
%define req_gimp_version 2.0

Summary:	Resynthesizer is a Gimp plug-in for texture synthesis	
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Graphics
URL:		http://www.logarithmic.net/pfh/resynthesizer
Source:		http://www.logarithmic.net/pfh-files/resynthesizer/%{plugin_name}-%{version}.tar.bz2

BuildRequires:	libgimp-devel >= %{req_gimp_version}

Requires:	gimp2_0 >= %{req_gimp_version}

%description
Resynthesizer is a Gimp plug-in for texture synthesis.
Given a sample of a texture, it can create more of that texture.
This has a surprising number of uses:
    * Creating more of a texture
    * Removing objects from images
    * Creating themed images

%prep
%setup -q -n %{plugin_name}-%{version}

%build
%make GIMPTOOL=gimptool-2.0

%install
rm -rf %{buildroot}
GIMPPLUGINPDIR=$RPM_BUILD_ROOT/`gimptool-2.0 --gimpplugindir`/plug-ins
GIMPSCRIPTDIR=$RPM_BUILD_ROOT/`gimptool-2.0 --gimpdatadir`/scripts
mkdir -p $GIMPPLUGINPDIR
mkdir -p $GIMPSCRIPTDIR
install -m 755 resynth $GIMPPLUGINPDIR
install -m 755 *scm $GIMPSCRIPTDIR

%clean
rm -rf %{buildroot}

%files 
%defattr(-, root, root)
%doc COPYING README
%{_libdir}/gimp/2.0/plug-ins/*
%{_datadir}/gimp/2.0/scripts/*



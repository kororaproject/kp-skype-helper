Name:		skype-helper
Version:	0.1
Release:	1%{?dist}
Summary:	Metapackage to handle Skype dependencies.
License:	GPLv3+
BuildArch:      noarch
Requires:	alsa-lib(x86-32) dbus-libs(x86-32) expat(x86-32) fontconfig(x86-32) freetype(x86-32) freetype-freeworld(x86-32) glib2(x86-32) glibc(x86-32) keyutils-libs(x86-32) krb5-libs(x86-32) libcom_err(x86-32) libgcc(x86-32) libICE(x86-32) libpng(x86-32) libselinux(x86-32) libSM(x86-32) libstdc++(x86-32) libuuid(x86-32) libX11(x86-32) libXau(x86-32) libxcb(x86-32) libXcursor(x86-32) libXext(x86-32) libXfixes(x86-32) libXi(x86-32) libXinerama(x86-32) libXrandr(x86-32) libXrender(x86-32) libXScrnSaver(x86-32) libXv(x86-32) openssl(x86-32) qt(x86-32) qt-x11(x86-32) zlib(x86-32) 

%description
This will NOT install Skype - it installs the dependencies for you
so that you can then download and install Skype from their website.

%install

%post
echo -e "\n##########\nNow you can download and install the Skype RPM from their website:\nhttp://www.skype.com/intl/en/get-skype/on-your-computer/linux/downloading.fedora\n##########"

%files

%changelog
* Wed Oct 11 2011 Chris Smart <chris@kororaa.org> 0.1-1
- Basic spec file to install Skype dependencies.




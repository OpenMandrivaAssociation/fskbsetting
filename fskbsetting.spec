Name:           fskbsetting
Version:        0.3
Release:        %mkrel 4
License:        GPLv3
Summary:        GUI Front-end for setxkbmap Command
URL:            http://forum.runtu.org/index.php/topic,5579.0.html
Group:          System/X11
Source0:        %{name}-%{version}.tar.bz2
# PATCH-FIX-OPENSUSE fskbsetting-0.3-desktop.patch lazy.kent.suse@gmail.com
# -- correct desktop-file
Patch0:         fskbsetting-0.3-desktop.patch
Patch1:		fskbsetting.autostart.patch
BuildRequires:  gcc-c++ intltool automake
BuildRequires: %{_lib}wxgtk2.8-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
fsKBSetting is GUI front-end for setxkbmap command.

%prep
%setup -q
%patch0
%patch1

%build
autoreconf --force --install --symlink
%configure
%{__make} %{?jobs:-j %jobs}

%install

rm -rf %{buildroot}

%{makeinstall}
mkdir %{buildroot}%{_datadir}/pixmaps
%{__rm} -rf %{buildroot}%{_prefix}/doc/%{name}
%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README TRANSLATORS
%{_datadir}/%{name}
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop

Name:           fskbsetting
Version:        0.3.1
Release:        %mkrel 1
License:        GPLv3
Summary:        GUI Front-end for setxkbmap Command
URL:            http://code.google.com/p/mandriva-lxde
Group:          System/X11
Source0:        http://mandriva-lxde.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++ intltool automake
BuildRequires: %{_lib}wxgtk2.8-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
fsKBSetting is GUI front-end for setxkbmap command.

%prep
%setup -q

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

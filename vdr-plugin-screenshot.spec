%define plugin	screenshot

Summary:	VDR plugin: Takes screenshots
Name:		vdr-plugin-%plugin
Version:	0.0.13
Release:	5
Group:		Video
License:	GPL
URL:		https://www.joachim-wilke.de/vdr-screenshot.htm
Source:		vdr-%plugin-%{version}.tar.bz2
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
With this plugin you can take still images of your screen. After installing
the plugin, a new mainmenu entry "Screenshot" will show up. Each time you
select this item, a file /tmp/title-yyyymmdd-hhmmss.jpg will be created,
where title is the current transmission or the recording currently replayed.

%prep
%setup -q -n %plugin-%{version}
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
%vdr_plugin_install

%files -f %plugin.vdr
%doc README HISTORY





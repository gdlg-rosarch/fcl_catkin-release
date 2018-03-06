Name:           ros-kinetic-fcl-catkin
Version:        0.5.91
Release:        0%{?dist}
Summary:        ROS fcl_catkin package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       libccd
Requires:       ros-kinetic-octomap
BuildRequires:  eigen3-devel
BuildRequires:  libccd
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-octomap

%description
fcl_catkin

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Tue Mar 06 2018 Wolfgang Merkt <w.merkt+oss@gmail.com> - 0.5.91-0
- Autogenerated by Bloom

* Mon Oct 30 2017 Wolfgang Merkt <w.merkt+oss@gmail.com> - 0.5.90-6
- Autogenerated by Bloom

* Mon Oct 30 2017 Wolfgang Merkt <w.merkt+oss@gmail.com> - 0.5.90-5
- Autogenerated by Bloom

* Mon Oct 30 2017 Wolfgang Merkt <w.merkt+oss@gmail.com> - 0.5.90-4
- Autogenerated by Bloom

* Fri Oct 27 2017 Wolfgang Merkt <w.merkt+oss@gmail.com> - 0.5.90-3
- Autogenerated by Bloom

* Fri Oct 27 2017 Wolfgang Merkt <w.merkt+oss@gmail.com> - 0.5.90-2
- Autogenerated by Bloom

* Thu Oct 26 2017 Wolfgang Merkt <w.merkt+oss@gmail.com> - 0.5.90-1
- Autogenerated by Bloom

* Wed Oct 18 2017 Wolfgang Merkt <w.merkt+oss@gmail.com> - 0.5.90-0
- Autogenerated by Bloom


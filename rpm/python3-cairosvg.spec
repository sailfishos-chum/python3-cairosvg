Name:       python3-cairosvg
Summary:    Mako template library for Python 3
Version:    2.5.2+git1
Release:    1
License:    LGPL3
URL:        https://github.com/Kozea/CairoSVG
Source0:    %{name}-%{version}.tar.bz2
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-cairocffi
BuildRequires:  python3-cssselect2
BuildRequires:  python3-defusedxml
BuildRequires:  python3dist(pillow)
BuildRequires:  python3-tinycss2
BuildRequires:  python3dist(pip)
# Required for rendering fonts inside an svg
Requires:  sailfish-fonts


%description
CairoSVG is an SVG converter based on Cairo. It can export SVG files to PDF,
EPS, PS, and PNG files.

%prep
%autosetup -n %{name}-%{version}/upstream
# skip pytest
sed -e 's/pytest-runner//' -i setup.cfg

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc README.rst NEWS.rst
%{_bindir}/*
%{python3_sitelib}/*

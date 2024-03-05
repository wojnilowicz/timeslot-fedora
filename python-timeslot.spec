# pypi_source doesn't have tests
%bcond tests 0

%global srcname timeslot
%global common_description %{expand:
Completes the Python datetime module: datetime (a time), timedelta (a duration), timezone (an offset), timeslot (a range/interval).

Supports operations such as: overlaps, intersects, contains, intersection, adjacent, gap, union.

Initially developed as part of aw-core, and inspired by a similar library for .NET.

You might also be interested in pandas.Interval.}

Name:           python-%{srcname}
Version:        0.1.2
Release:        1%{?dist}
Summary:        Class for working with time slots that have an arbitrary start and end.
License:        MIT
URL:            https://github.com/ErikBjare/timeslot
Source0:        %pypi_source
BuildArch:      noarch


%description %{common_description}


%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel


%description -n python3-%{srcname} %{common_description}


%prep
%autosetup -n %{srcname}-%{version}

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i '/^[[:blank:]]*"pytest-cov\b/d' pyproject.toml
sed -r -i '/^[[:blank:]]*"covdefaults\b/d' pyproject.toml


%generate_buildrequires
%pyproject_buildrequires -w %{?with_tests:-x test}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
%if %{with tests}
%pytest
%else
%pyproject_check_import
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md


%changelog
* Mon Mar 04 2024 Łukasz Wojniłowicz <lukasz.wojnilowicz@gmail.com> - 0.1.2-1
- Initial package

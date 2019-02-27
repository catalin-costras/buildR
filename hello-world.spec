Name:       hello-world
Version:    1
Release:    1
Summary:    Most simple RPM package
License:    FIXME

%description
This is my first RPM package, which does nothing.

%prep
# we have no source, so nothing here

%build
cat > hello-world.sh <<EOF
#!/usr/bin/bash
echo Hello world
EOF

%install
mkdir -p %{buildroot}/usr/local/bin
install -m 755 hello-world.sh %{buildroot}/usr/local/bin/hello-world.sh

%files
/usr/local/bin/hello-world.sh

%changelog
# let skip this for now

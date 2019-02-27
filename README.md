# buildR
Build RPMs with docker and packer them

## Techs
- packer: custom iso creation
- jc21/docker-rpmbuild-centos7: dockerfile with all the dependencies to build RPMs
- liahimn/rpmbuilds: addition of createrepo package to the above 
- centos 7.6 minimal iso, or it will be downloaded

## Up and Running
A brief up and running. More details can be taken from: jc21/docker-rpmbuild-centos7

## Build RPMS
The structure has to be already create in the working directory. 
### Build RPMs as per 
```bash
docker run \
    --name rpmbuild-centos7 \
    -v /path/to/your/rpmbuild:/home/rpmbuilder/rpmbuild \
    --rm=true \
    jc21/rpmbuild-centos7 \
    /bin/build-spec /home/rpmbuilder/rpmbuild/SPECS/something.spec
```

### Create repo
Copy the RPM created into the repo directory. Use createrepo or update
```bash
docker run \
    --name rpm-repo \
    -v /path/to/your/repo:/home/rpmbuilder/repo \
    --rm=true \
    liahimn/rpmbuilds \
    createrepo -v /home/rpmbuilder/rpmbuild/repo
```

### Repo webserver
Create an nginx conf including 'autoindex on'
```bash
docker run --name repo-nginx -p 80:80 -v /path/to/your/repo:/usr/share/nginx/html:ro -d nginx
```

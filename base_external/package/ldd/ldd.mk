# Assignment 7 Repo
LDD_VERSION = 2bd47d53c1163597b3665b99831ce59ff8f73e45
LDD_SITE = git@github.com:cu-ecen-5013/assignment-7-buildroot-and-yocto-kernel-builds-IMNG7.git
LDD_SITE_METHOD = git

LDD_MODULE_SUBDIRS = misc-modules
LDD_MODULE_SUBDIRS += scull

$(eval $(kernel-module))
$(eval $(generic-package))


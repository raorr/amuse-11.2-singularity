BootStrap: docker
From: nvidia/cuda:10.0-devel-ubuntu16.04

%environment
	FC=gfortran
	F77=gfortran

%post
	apt-get update && apt-get install -y git wget
	apt-get install -y build-essential curl g++ gfortran gettext zlib1g-dev

	wget https://github.com/amusecode/amuse/archive/release-11.2.tar.gz
	tar -xf release-11.2.tar.gz
	mv amuse-release-11.2/ /amuse/

	apt-get install -y build-essential gfortran python-dev \
	  openmpi-bin libopenmpi-dev \
	  libgsl0-dev cmake libfftw3-3 libfftw3-dev \
	  libgmp3-dev libmpfr-dev \
	  libhdf5-serial-dev hdf5-tools \
	  python-nose python-numpy python-setuptools python-docutils \
	  python-h5py python-setuptools git openjdk-8-jdk python-pip

	pip install cython scipy mpi4py
	
	echo "export PATH=/amuse/:${PATH}" >> /etc/profile

	cd /amuse/ && ./configure --enable-cuda --with-cuda-libdir=/usr/local/cuda/lib64
	cd /amuse/ && make DOWNLOAD_CODES=1

	chmod 755 /amuse/amuse.sh
	# make the home and data folders from ACCRE available for this image
	mkdir /scratch /data /gpfs22 /gpfs23

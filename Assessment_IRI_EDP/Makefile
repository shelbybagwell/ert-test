# Fortran compiler
FC = gfortran

# source code
TARFILE = 00_iri.zip
SRC_DIR = IRI-zip
SRC = $(SRC_DIR)/iritest.for $(SRC_DIR)/irisub.for $(SRC_DIR)/irifun.for \
		$(SRC_DIR)/iritec.for $(SRC_DIR)/iridreg.for $(SRC_DIR)/igrf.for \
		$(SRC_DIR)/cira.for $(SRC_DIR)/iriflip.for $(SRC_DIR)/rocdrift.for

# Flags for old fortan code and shared object
FFLAGS = -fPIC -std=legacy
SOFLAGS = -shared

# output
TARGET = libiri2020.so

all: $(TARGET)

$(TARGET): $(SRC)
	@echo "Compiling IRI Fortran source files into $@"
	$(FC) $(FFLAGS) $(SOFLAGS) -o $@ $(SRC)

$(SRC): extract

extract:
	@if [ ! -f $(TARFILE) ]; then \
		echo "$(TARFILE) not found."; \
		echo "Please download it from:"; \
		echo "http://irimodel.org/IRI-2020/00_iri.zip"; \
		echo "and place it in this directory."; \
		exit 1; \
	fi
	@if [ ! -d $(SRC_DIR) ]; then \
		echo "Extracting IRI source files into $(SRC_DIR)/..."; \
		unzip -q $(TARFILE); \
	fi

clean:
	rm -f *.o *.mod *.dylib
	rm -rf $(SRC_DIR)
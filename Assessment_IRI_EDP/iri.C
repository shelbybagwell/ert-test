#include<stdio.h>
#include<string.h>
#include<math.h>

/* 
Arguments are passed by reference in FORTRAN, so we need to use pointers.
From the irisub.for file:
INPUT:  JF(1:50)      true/false switches for several options
C         JMAG          =0 geographic   = 1 geomagnetic coordinates
C         ALATI,ALONG   LATITUDE NORTH AND LONGITUDE EAST IN DEGREES
C         IYYYY         Year as YYYY, e.g. 1985
C         MMDD (-DDD)   DATE (OR DAY OF YEAR AS A NEGATIVE NUMBER)
C         DHOUR         LOCAL TIME (OR UNIVERSAL TIME + 25) IN DECIMAL 
C                          HOURS
C         HEIBEG,       HEIGHT RANGE IN KM; maximal 100 heights, i.e.
C          HEIEND,HEISTP        int((heiend-heibeg)/heistp)+1.le.100
C
C    JF switches to turn off/on (.true./.false.) several options
C   OUTPUT:  OUTF(1:20,1:1000)
C               OUTF(1,*)  ELECTRON DENSITY/M-3
Reminder: fortran is column major, C is row major
*/
extern void iri_sub_(int jf[50], int *jmag, float *alati, float *along, 
                     int *iyyyy, int *mmdd, float *dhour, float *heibeg,
                     float *heiend, float *heistp, float outf[1000][20],
                     float oarr[100]);
extern void read_ig_rz_();
extern void readapf107_();

int main() {
    // Set parameters to call iri_sub_
    // From irisub.for:
    // jf(4,5,6,23,30,33,35,39,40,47)=.false. all others =.true.
    int jf[50];
    for (int i = 0; i < 50; i++) {
        jf[i] = 1; // default true
    }
    // Set specific options to false
    jf[4]  = 0;
    jf[5]  = 0;
    jf[6]  = 0;
    jf[23] = 0;
    jf[30] = 0;
    jf[33] = 0;
    jf[35] = 0;
    jf[39] = 0;
    jf[40] = 0;
    jf[47] = 0;
    // geographic coordinates
    int jmag = 0; 
    // location of interest: 37.8N, 75.4W
    float alati = 38.7;
    float along = -75.4;
    // Dates of interest: 2021-03-03 11:00:00; 2021-03-04 23:00:00
    int iyyyy = 2021;
    int mmdd_1 = 303;
    float dhour_1 = 11.0;
    int mmdd_2 = 304;
    float dhour_2 = 23.0;
    // altitude values, based on ionosphere range
    float heibeg = 100.0;
    float heiend = 1000.0;
    float heistp = 25.0;
    // declare output vars
    float outf[1000][20];
    float oarr[100];

    int npts = (int)((heiend - heibeg)/heistp) + 1; // altitude points
    
    // Read the data files
    read_ig_rz_();
    readapf107_();

    // Create data for 2021-03-03 11:00:00
    iri_sub_(jf, &jmag, &alati, &along, &iyyyy, &mmdd_1, &dhour_1, &heibeg, 
             &heiend, &heistp, outf, oarr);
    
    // Output the data to a file
    FILE *fp_1 = fopen("edp_output_2021-03-03.dat", "w");
    if (!fp_1) {
        perror("Could not write to file");
        return 1;
    }
    fprintf(fp_1, "# Alt (km) Electron Density (m^-3)\n");
    for (int i=0; i<npts; i++) {
        float height = heibeg + i * heistp;
        float ne = outf[i][0];
        // plasma frequency would be outf[i][14]
        fprintf(fp_1, "%.1f %.6e\n", height, ne);
    }
    fclose(fp_1);

    // Create data for 2021-03-04 23:00:00
    iri_sub_(jf, &jmag, &alati, &along, &iyyyy, &mmdd_2, &dhour_2, &heibeg, 
             &heiend, &heistp, outf, oarr);
    // Output the data to a file
    FILE *fp_2 = fopen("edp_output_2021-03-04.dat", "w");
    if (!fp_2) {
        perror("Could not write to file");
        return 1;
    }
    fprintf(fp_2, "# Alt (km) Electron Density (m^-3)\n");
    for (int i=0; i<npts; i++) {
        float height = heibeg + i * heistp;
        float ne = outf[i][0];
        // plasma frequency would be outf[i][14]
        fprintf(fp_1, "%.1f %.6e\n", height, ne);
    }
    fclose(fp_2);

    printf("EDP data successfully created\n");
    return 0;
}
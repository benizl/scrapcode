#include <visp/vpImageConvert.h>
#include <visp/vpKltOpencv.h>
#include <visp/vpDisplayOpenCV.h>
#include <visp/vpVideoReader.h>
int main()
{
#if (VISP_HAVE_OPENCV_VERSION < 0x010100)
#error "OpenCV Version" $VISP_HAVE_OPENCV_VERSION
#endif

#ifndef VISP_HAVE_FFMPEG
#error "No FFMPEG"
#endif

try {
vpVideoReader reader;
reader.setFileName("/usr/local/image/ViSP-images/video/cube.mpeg");
vpImage<unsigned char> I;
reader.acquire(I);
IplImage * cvI = NULL;
vpImageConvert::convert(I, cvI);
// Display initialisation
vpDisplayOpenCV d(I, 0, 0, "Klt tracking");
vpDisplay::display(I);
vpDisplay::flush(I);
vpKltOpencv tracker;
// Set tracker parameters
tracker.setMaxFeatures(200);
tracker.setWindowSize(10);
tracker.setQuality(0.01);
tracker.setMinDistance(15);
tracker.setHarrisFreeParameter(0.04);
tracker.setBlockSize(9);
tracker.setUseHarris(1);
tracker.setPyramidLevels(3);
// Initialise the tracking
tracker.initTracking(cvI);
while ( ! reader.end() )
{
reader.acquire(I);
vpDisplay::display(I);
vpImageConvert::convert(I, cvI);
tracker.track(cvI);
tracker.display(I, vpColor::red);
vpDisplay::flush(I);
}
vpDisplay::getClick(I);
cvReleaseImage(&cvI);
return 0;
}
catch(vpException e) {
std::cout << "Catch an exception: " << e << std::endl;
}

}


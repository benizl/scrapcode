
#include <visp/vp1394CMUGrabber.h>
#include <visp/vp1394TwoGrabber.h>
#include <visp/vpV4l2Grabber.h>
#include <visp/vpDisplayGDI.h>
#include <visp/vpDisplayX.h>
#include <visp/vpMeLine.h>
int main()
{
	try {
		vpImage<unsigned char> I;

		vpV4l2Grabber g;

		g.open(I);
		g.acquire(I);

		vpDisplayX d(I, 0, 0, "Camera view");

		vpDisplay::display(I);
		vpDisplay::flush(I);
		vpMe me;
		me.setRange(10);
		me.setThreshold(15000);
		me.setSampleStep(5);
		vpMeLine line;
		line.setMe(&me);
		line.setDisplay(vpMeSite::RANGE_RESULT);
		line.initTracking(I);

		while(1) {
			g.acquire(I);
			vpDisplay::display(I);
			line.track(I);
			line.display(I, vpColor::red);
			vpDisplay::flush(I);
		}
	} catch(vpException e) {
		std::cout << "Catch an exception: " << e << std::endl;
	}
}


import React from 'react';

class MainMenu extends React.Component {
   render() {
      return (
        <div className={"container-fluid"} data-aos="fade" data-aos-delay="500">
          <div className={"swiper-container images-carousel"}>
              <div className={"swiper-wrapper"}>
                  <div className={"swiper-slide"}>
                    <div className={"image-wrap"}>
                      <div className={"image-info"}>
                        <h2 className={"mb-3"}>Nature</h2>
                        <a href={"single.html"} className={"btn btn-outline-white py-2 px-4"}>More Photos</a>
                      </div>
                       <img src={"https://colorlib.com/preview/theme/photon/images/img_1.jpg"} />
                    </div>
                  </div>
                  <div className={"swiper-slide"}>
                    <div className={"image-wrap"}>
                      <div className={"image-info"}>
                        <h2 className={"mb-3"}>Portrait</h2>
                        <a href="single.html" className={"btn btn-outline-white py-2 px-4"}>More Photos</a>
                      </div>
                    </div>
                  </div>
                  <div className={"swiper-slide"}>
                    <div className={"image-wrap"}>
                      <div className={"image-info"}>
                        <h2 className={"mb-3"}>People</h2>
                        <a href="single.html" className={"btn btn-outline-white py-2 px-4"}>More Photos</a>
                      </div>
                    </div>
                  </div>
                  <div className={"swiper-slide"}>
                    <div className={"image-wrap"}>
                      <div className={"image-info"}>
                        <h2 className={"mb-3"}>Architecture</h2>
                        <a href="single.html" className={"btn btn-outline-white py-2 px-4"}>More Photos</a>
                      </div>
                    </div>
                  </div>
                  <div className={"swiper-slide"}>
                    <div className={"image-wrap"}>
                      <div className={"image-info"}>
                        <h2 className={"mb-3"}>Animals</h2>
                        <a href="single.html" className={"btn btn-outline-white py-2 px-4"}>More Photos</a>
                      </div>
                    </div>
                  </div>
                  <div className={"swiper-slide"}>
                    <div className={"image-wrap"}>
                      <div className={"image-info"}>
                        <h2 className={"mb-3"}>Sports</h2>
                        <a href="single.html" className={"btn btn-outline-white py-2 px-4"}>More Photos</a>
                      </div>
                    </div>
                  </div>
                  <div className={"swiper-slide"}>
                    <div className={"image-wrap"}>
                      <div className={"image-info"}>
                        <h2 className={"mb-3"}>Travel</h2>
                        <a href="single.html" className={"btn btn-outline-white py-2 px-4"}>More Photos</a>
                      </div>
                    </div>
                  </div>
              </div>

              <div className={"swiper-pagination"}></div>
              <div className={"swiper-button-prev"}></div>
              <div className={"swiper-button-next"}></div>
              <div className={"swiper-scrollbar"}></div>
          </div>
        </div>
      )
   }
 }
export default MainMenu;

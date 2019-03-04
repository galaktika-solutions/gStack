import React from 'react';
import MainMenu from './main_menu.jsx';

class Core extends React.Component {
   render() {
      return (
        <div>
         <div className={"site-wrap"}>
           <div className={"site-mobile-menu"}>
             <div className={"site-mobile-menu-header"}>
               <div className={"site-mobile-menu-close mt-3"}>
                 <span className={"icon-close2 js-menu-toggle"}></span>
               </div>
             </div>
             <div className={"site-mobile-menu-body"}></div>
           </div>
         </div>

         <header className={"site-navbar py-3"} role={"banner"}>

           <div className={"container-fluid"}>
             <div className={"row align-items-center"}>

               <div className={"col-6 col-xl-2"} dataaos={"fade-down"}>
                 <h1 className={"mb-0"}><a href="index.html" className={"text-black h2 mb-0"}>Photon</a></h1>
               </div>
               <div className={"col-10 col-md-8 d-none d-xl-block"} dataaos={"fade-down"}>
                 <nav className={"site-navigation position-relative text-right text-lg-center"} role={"navigation"}>

                   <ul className={"site-menu js-clone-nav mx-auto d-none d-lg-block"}>
                     <li className={"active"}><a href="index.html">Home</a></li>
                     <li className={"has-children"}>
                       <a href="single.html">Gallery</a>
                       <ul className={"dropdown"}>
                         <li><a href="#">Nature</a></li>
                         <li><a href="#">Portrait</a></li>
                         <li><a href="#">People</a></li>
                         <li><a href="#">Architecture</a></li>
                         <li><a href="#">Animals</a></li>
                         <li><a href="#">Sports</a></li>
                         <li><a href="#">Travel</a></li>
                         <li className={"has-children"}>
                           <a href="#">Sub Menu</a>
                           <ul className={"dropdown"}>
                             <li><a href="#">Menu One</a></li>
                             <li><a href="#">Menu Two</a></li>
                             <li><a href="#">Menu Three</a></li>
                           </ul>
                         </li>
                       </ul>
                     </li>
                     <li><a href="services.html">Services</a></li>
                     <li><a href="about.html">About</a></li>
                     <li><a href="contact.html">Contact</a></li>
                   </ul>
                 </nav>
               </div>

               <div className={"col-6 col-xl-2 text-right"} dataaos={"fade-down"}>
                 <div className={"d-none d-xl-inline-block"}>
                   <ul className={"site-menu js-clone-nav ml-auto list-unstyled d-flex text-right mb-0"} dataclass={"social"}>
                     <li>
                       <a href="#" className={"pl-0 pr-3"}><span className={"icon-facebook"}></span></a>
                     </li>
                     <li>
                       <a href="#" className={"pl-3 pr-3"}><span className={"icon-twitter"}></span></a>
                     </li>
                     <li>
                       <a href="#" className={"pl-3 pr-3"}><span className={"icon-instagram"}></span></a>
                     </li>
                     <li>
                       <a href="#" className={"pl-3 pr-3"}><span className={"icon-youtube-play"}></span></a>
                     </li>
                   </ul>
                 </div>

                 <div className={"d-inline-block d-xl-none ml-md-0 mr-auto py-3"} style={{position: "relative", top: "3px"}}><a href="#" className={"site-menu-toggle js-menu-toggle text-black"}><span className={"icon-menu h3"}></span></a></div>

               </div>

             </div>
           </div>

         </header>

         <MainMenu />

         <div className={"footer py-4"}>
           <div className={"container-fluid"}>
             <p>
             Copyright &copy;<script data-cfasync="false" src="/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script>document.write(new Date().getFullYear());</script> All rights reserved | This template is made with <i className="icon-heart-o" aria-hidden="true"></i> by <a href="https://colorlib.com" target="_blank" >Colorlib</a>
             </p>
           </div>
         </div>
         </div>
      );
   }
}
export default Core;

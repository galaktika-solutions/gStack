/* global gettext, config, gettext, $ */
import React from "react";
import BlockUi from "react-block-ui";
import {Loader} from "react-loaders";
import Dropdown from "react-bootstrap/Dropdown";
import Carousel from "react-bootstrap/Carousel";
import _ from "lodash";
import {default as MultiCarousel} from "react-multi-carousel";

import Ajax from "./ajax.jsx";
import AbortRequests from "../utils/abort_requests.js";

class Dashboard extends React.PureComponent {
  /* ***************************** */
  /* ** REACT LIFECYCLE METHODS ** */
  /* ***************************** */

  constructor(props) {
    super(props);
    window.title = gettext("Dashboard");
    this.requests = [];
    this.state = {
      data: [],
      blocking: true
    };
  }

  componentDidMount() {
    console.log(config);
    Ajax({
      url: "/api/core/key_value_store/",
      statusCode: {
        200: response => this.setState({data: response})
      }
    });
    setTimeout(
      () =>
        this.setState({blocking: false}, () =>
          $(".mobile-menu").slicknav({
            prependTo: "#mobile-menu-wrap",
            allowParentLinks: true
          })
        ),
      1000
    );
  }

  componentWillUnmount() {
    AbortRequests(this.requests);
  }

  onLanguageChange(eventkey) {
    this.requests.push(
      Ajax({
        url: "/i18n/setlang/",
        type: "POST",
        data: {language: eventkey},
        statusCode: {
          204: () => window.location.reload()
        }
      })
    );
  }

  /* ***************** */
  /* ** MAIN RENDER ** */
  /* ***************** */

  render() {
    return (
      <BlockUi
        tag="div"
        id="preloder"
        style={this.state.blocking ? {} : {backgroundColor: "transparent"}}
        blocking={this.state.blocking}
        renderChildren={false}
        loader={<Loader active type="ball-clip-rotate" color="#02a17c" />}
      >
        {/* <!-- Header Section Begin --> */}
        <header className="header-section">
          <div className="header-top">
            <div className="container">
              <div className="ht-left">
                <div className="mail-service">
                  <i className=" fa fa-envelope" />
                  hello.colorlib@gmail.com
                </div>
                <div className="phone-service">
                  <i className=" fa fa-phone" />
                  +65 11.188.888
                </div>
              </div>
              <div className="ht-right">
                <a href="#" className="login-panel">
                  <i className="fa fa-user" />
                  Login
                </a>
                <div className="lan-selector">
                  <Dropdown onSelect={eventkey => this.onLanguageChange(eventkey)}>
                    <Dropdown.Toggle variant="language-selector" id="dropdown-basic">
                      <span
                        className={`flag-icon flag-icon-${config.flagMap[config.currentLanguage]}`}
                        style={{marginRight: "3px"}}
                      />
                      {_.find(config.languages, o => o[0] === config.currentLanguage)[1]}
                    </Dropdown.Toggle>
                    <Dropdown.Menu>
                      {_.map(
                        _.filter(config.languages, o => o[0] !== config.currentLanguage),
                        item => (
                          <Dropdown.Item
                            key={item[0]}
                            eventKey={item[0]}
                            style={{padding: "0px .75rem"}}
                          >
                            <span
                              className={`flag-icon flag-icon-${config.flagMap[item[0]]}`}
                              style={{marginRight: "3px"}}
                            />
                            {item[1]}
                          </Dropdown.Item>
                        )
                      )}
                    </Dropdown.Menu>
                  </Dropdown>
                </div>
                <div className="top-social">
                  <a href="#">
                    <i className="ti ti-facebook" />
                  </a>
                  <a href="#">
                    <i className="ti ti-twitter-alt" />
                  </a>
                  <a href="#">
                    <i className="ti ti-linkedin" />
                  </a>
                  <a href="#">
                    <i className="ti ti-pinterest" />
                  </a>
                </div>
              </div>
            </div>
          </div>
          <div className="container">
            <div className="inner-header">
              <div className="row">
                <div className="col-lg-2 col-md-2">
                  <div className="logo">
                    <a href="#/">
                      <img src={`${config.staticUrl}images/logo.png`} alt="" />
                    </a>
                  </div>
                </div>
                <div className="col-lg-7 col-md-7">
                  <div className="advanced-search">
                    <button type="button" className="category-btn">
                      {gettext("All Categories")}
                    </button>
                    <div className="input-group">
                      <input type="text" placeholder="What do you need?" />
                      <button type="button">
                        <i className="ti ti-search" />
                      </button>
                    </div>
                  </div>
                </div>
                <div className="col-lg-3 text-right col-md-3">
                  <ul className="nav-right">
                    <li className="heart-icon">
                      <a href="#">
                        <i className="icon_heart_alt" />
                        <span>1</span>
                      </a>
                    </li>
                    <li className="cart-icon">
                      <a href="#">
                        <i className="icon_bag_alt" />
                        <span>3</span>
                      </a>
                      <div className="cart-hover">
                        <div className="select-items">
                          <table>
                            <tbody>
                              <tr>
                                <td className="si-pic">
                                  <img
                                    src={`${config.staticUrl}images/select-product-1.jpg`}
                                    alt=""
                                  />
                                </td>
                                <td className="si-text">
                                  <div className="product-selected">
                                    <p>$60.00 x 1</p>
                                    <h6>Kabino Bedside Table</h6>
                                  </div>
                                </td>
                                <td className="si-close">
                                  <i className="ti ti-close" />
                                </td>
                              </tr>
                              <tr>
                                <td className="si-pic">
                                  <img
                                    src={`${config.staticUrl}images/select-product-2.jpg`}
                                    alt=""
                                  />
                                </td>
                                <td className="si-text">
                                  <div className="product-selected">
                                    <p>$60.00 x 1</p>
                                    <h6>Kabino Bedside Table</h6>
                                  </div>
                                </td>
                                <td className="si-close">
                                  <i className="ti ti-close" />
                                </td>
                              </tr>
                            </tbody>
                          </table>
                        </div>
                        <div className="select-total">
                          <span>{gettext("total:")}</span>
                          <h5>$120.00</h5>
                        </div>
                        <div className="select-button">
                          <a href="#" className="primary-btn view-card">
                            {gettext("VIEW CARD")}
                          </a>
                          <a href="#" className="primary-btn checkout-btn">
                            {gettext("CHECK OUT")}
                          </a>
                        </div>
                      </div>
                    </li>
                    <li className="cart-price">$150.00</li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
          <div className="nav-item">
            <div className="container">
              <div className="nav-depart">
                <div className="depart-btn">
                  <i className="ti ti-menu" />
                  <span>{gettext("All departments")}</span>
                  <ul className="depart-hover">
                    <li className="active">
                      <a href="#">{gettext("Women’s Clothing")}</a>
                    </li>
                    <li>
                      <a href="#">{gettext("Men’s Clothing")}</a>
                    </li>
                    <li>
                      <a href="#">{gettext("Underwear")}</a>
                    </li>
                    <li>
                      <a href="#">{gettext("Kid's Clothing")}</a>
                    </li>
                    <li>
                      <a href="#">Brand Fashion</a>
                    </li>
                    <li>
                      <a href="#">Accessories/Shoes</a>
                    </li>
                    <li>
                      <a href="#">Luxury Brands</a>
                    </li>
                    <li>
                      <a href="#">Brand Outdoor Apparel</a>
                    </li>
                  </ul>
                </div>
              </div>
              <nav className="nav-menu mobile-menu">
                <ul>
                  <li className="active">
                    <a href="./index.html">Home</a>
                  </li>
                  <li>
                    <a href="./shop.html">Shop</a>
                  </li>
                  <li>
                    <span>Collection</span>
                    <ul className="dropdown">
                      <li>
                        <a href="#">Men's</a>
                      </li>
                      <li>
                        <a href="#">Women's</a>
                      </li>
                      <li>
                        <a href="#">Kid's</a>
                      </li>
                    </ul>
                  </li>
                  <li>
                    <a href="./blog.html">Blog</a>
                  </li>
                  <li>
                    <a href="./contact.html">Contact</a>
                  </li>
                  <li>
                    <span>Pages</span>
                    <ul className="dropdown">
                      <li>
                        <a href="./blog-details.html">Blog Details</a>
                      </li>
                      <li>
                        <a href="./shopping-cart.html">Shopping Cart</a>
                      </li>
                      <li>
                        <a href="./check-out.html">Checkout</a>
                      </li>
                      <li>
                        <a href="./faq.html">Faq</a>
                      </li>
                      <li>
                        <a href="./register.html">Register</a>
                      </li>
                      <li>
                        <a href="./login.html">Login</a>
                      </li>
                    </ul>
                  </li>
                </ul>
              </nav>
              <div id="mobile-menu-wrap" />
            </div>
          </div>
        </header>
        {/* <!-- Hero Section Begin --> */}
        <Carousel>
          <Carousel.Item>
            <img
              className="d-block w-100"
              src={`${config.staticUrl}images/hero-1.jpg`}
              alt="First slide"
            />
            <Carousel.Caption className="col-12 col-md-4 hero-items">
              <div className="single-hero-items">
                <span>Bag,kids</span>
                <h1>Black friday</h1>
                <p>
                  Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor
                  incididunt ut labore et dolore
                </p>
                <a href="#" className="primary-btn">
                  Shop Now
                </a>
                <div className="off-card">
                  <h2>
                    Sale <span>50%</span>
                  </h2>
                </div>
              </div>
            </Carousel.Caption>
          </Carousel.Item>
          <Carousel.Item>
            <img
              className="d-block w-100"
              src={`${config.staticUrl}images/hero-2.jpg`}
              alt="First slide"
            />
            <Carousel.Caption className="col-12 col-md-4 hero-items">
              <div className="single-hero-items">
                <span>Bag,kids</span>
                <h1>Black friday</h1>
                <p>
                  Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor
                  incididunt ut labore et dolore
                </p>
                <a href="#" className="primary-btn">
                  Shop Now
                </a>
                <div className="off-card">
                  <h2>
                    Sale <span>50%</span>
                  </h2>
                </div>
              </div>
            </Carousel.Caption>
          </Carousel.Item>
        </Carousel>
        {/* <!-- Hero Section End --> */}

        {/* <!-- Banner Section Begin --> */}
        <div className="banner-section spad">
          <div className="container-fluid">
            <div className="row">
              <div className="col-lg-4">
                <div className="single-banner">
                  <img src={`${config.staticUrl}images/banner-1.jpg`} alt="" />
                  <div className="inner-text">
                    <h4>Men’s</h4>
                  </div>
                </div>
              </div>
              <div className="col-lg-4">
                <div className="single-banner">
                  <img src={`${config.staticUrl}images/banner-2.jpg`} alt="" />
                  <div className="inner-text">
                    <h4>Women’s</h4>
                  </div>
                </div>
              </div>
              <div className="col-lg-4">
                <div className="single-banner">
                  <img src={`${config.staticUrl}images/banner-3.jpg`} alt="" />
                  <div className="inner-text">
                    <h4>Kid’s</h4>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        {/* <!-- Banner Section End --> */}

        {/* <!-- Women Banner Section Begin --> */}
        <section className="women-banner spad">
          <div className="container-fluid">
            <div className="row">
              <div className="col-lg-3">
                <div
                  className="product-large"
                  style={{
                    backgroundImage: `url(${config.staticUrl}images/products/women-large.jpg)`
                  }}
                >
                  <h2>Women’s</h2>
                  <a href="#">Discover More</a>
                </div>
              </div>
              <div className="col-lg-8 offset-lg-1">
                <div className="filter-control">
                  <ul>
                    <li className="active">Clothings</li>
                    <li>HandBag</li>
                    <li>Shoes</li>
                    <li>Accessories</li>
                  </ul>
                </div>
                <MultiCarousel
                  infinite={true}
                  autoPlay={true}
                  draggable={false}
                  autoPlaySpeed={4000}
                  responsive={{
                    superLargeDesktop: {
                      // the naming can be any, depends on you.
                      breakpoint: {max: 4000, min: 3000},
                      items: 5
                    },
                    desktop: {
                      breakpoint: {max: 3000, min: 1024},
                      items: 3
                    },
                    tablet: {
                      breakpoint: {max: 1024, min: 464},
                      items: 2
                    },
                    mobile: {
                      breakpoint: {max: 464, min: 0},
                      items: 1
                    }
                  }}
                >
                  <div style={{padding: "0px 10px"}}>
                    <img
                      className="d-block w-100"
                      src={`${config.staticUrl}images/products/women-1.jpg`}
                      alt="First slide"
                    />
                    <div className="product-item">
                      <div className="pi-pic">
                        <div className="sale">Sale</div>
                      </div>
                      <div className="pi-text">
                        <div className="catagory-name">Coat</div>
                        <a href="#">
                          <h5>Pure Pineapple</h5>
                        </a>
                        <div className="product-price">
                          $14.00
                          <span>$35.00</span>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div style={{padding: "0px 10px"}}>
                    <img
                      className="d-block w-100"
                      src={`${config.staticUrl}images/products/women-2.jpg`}
                      alt="First slide"
                    />
                    <div className="product-item">
                      <div className="pi-pic">
                        <div className="sale">Sale</div>
                      </div>
                      <div className="pi-text">
                        <div className="catagory-name">Coat</div>
                        <a href="#">
                          <h5>Pure Pineapple</h5>
                        </a>
                        <div className="product-price">
                          $14.00
                          <span>$35.00</span>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div style={{padding: "0px 10px"}}>
                    <img
                      className="d-block w-100"
                      src={`${config.staticUrl}images/products/women-3.jpg`}
                      alt="First slide"
                    />
                    <div className="product-item">
                      <div className="pi-pic">
                        <div className="sale">Sale</div>
                      </div>
                      <div className="pi-text">
                        <div className="catagory-name">Coat</div>
                        <a href="#">
                          <h5>Pure Pineapple</h5>
                        </a>
                        <div className="product-price">
                          $14.00
                          <span>$35.00</span>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div style={{padding: "0px 10px"}}>
                    <img
                      className="d-block w-100"
                      src={`${config.staticUrl}images/products/women-4.jpg`}
                      alt="First slide"
                    />
                    <div className="product-item">
                      <div className="pi-pic">
                        <div className="sale">Sale</div>
                      </div>
                      <div className="pi-text">
                        <div className="catagory-name">Coat</div>
                        <a href="#">
                          <h5>Pure Pineapple</h5>
                        </a>
                        <div className="product-price">
                          $14.00
                          <span>$35.00</span>
                        </div>
                      </div>
                    </div>
                  </div>
                </MultiCarousel>
              </div>
            </div>
          </div>
        </section>
        {/* <!-- Women Banner Section End --> */}
        <div style={{height: "4000px"}}>
          asd
          <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br />
          <br /> <br /> <br /> <br /> <br /> <br />
        </div>
      </BlockUi>
    );
  }
}

export default Dashboard;

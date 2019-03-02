import React, { Component } from 'react';

class App extends Component {
  render() {
    return (
      <div className="App">
      <header id="header">
        <div className="inner">
          <a href="#" className="image avatar"><img src="images/avatar.jpg" alt="" /></a>
          <h1><strong>I am Strata</strong>, a super simple<br/>
          responsive site template freebie<br/>
          crafted by <a href="http://html5up.net">HTML5 UP</a>.</h1>
        </div>
        <div className="login-page">
          <div className="form">
            <form className="login-form">
              <input type="text" placeholder="ticker symbol"/>
              <input type="number" placeholder="number of shares"/>
              <button>submit</button>
            </form>
          </div>
        </div>
      </header>
      <div id="main">
          <section id="one">
            <header className="major">
              <h2>Ipsum lorem dolor aliquam ante commodo<br />
              magna sed accumsan arcu neque.</h2>
            </header>
            <p>Accumsan orci faucibus id eu lorem semper. Eu ac iaculis ac nunc nisi lorem vulputate lorem neque cubilia ac in adipiscing in curae lobortis tortor primis integer massa adipiscing id nisi accumsan pellentesque commodo blandit enim arcu non at amet id arcu magna. Accumsan orci faucibus id eu lorem semper nunc nisi lorem vulputate lorem neque cubilia.</p>
            <ul className="actions">
              <li><a href="#" className="button">Learn More</a></li>
            </ul>
          </section>
      </div>
      <footer id="footer">
        <div className="inner">
          <ul className="icons">
            <li><a href="#" className="icon fa-twitter"><span className="label">Twitter</span></a></li>
            <li><a href="#" className="icon fa-github"><span className="label">Github</span></a></li>
            <li><a href="#" className="icon fa-dribbble"><span className="label">Dribbble</span></a></li>
            <li><a href="#" className="icon fa-envelope-o"><span className="label">Email</span></a></li>
          </ul>
          <ul className="copyright">
            <li>&copy; Untitled</li><li>Design: <a href="http://html5up.net">HTML5 UP</a></li>
          </ul>
        </div>
      </footer>
      <script src="assets/js/jquery.min.js"></script>
      <script src="assets/js/jquery.poptrox.min.js"></script>
      <script src="assets/js/browser.min.js"></script>
      <script src="assets/js/breakpoints.min.js"></script>
      <script src="assets/js/util.js"></script>
      <script src="assets/js/main.js"></script>

      </div>
    );
  }
}

export default App;

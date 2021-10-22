/*!

=========================================================
* Black Dashboard React v1.2.0
=========================================================

* Product Page: https://www.creative-tim.com/product/black-dashboard-react
* Copyright 2020 Creative Tim (https://www.creative-tim.com)
* Licensed under MIT (https://github.com/creativetimofficial/black-dashboard-react/blob/master/LICENSE.md)

* Coded by Creative Tim

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/
import React from "react";

// reactstrap components
import {Row, Col, Button} from "reactstrap";
import {Image} from "antd";

function ImageValidator() {
    return (
        <>
            <div className="content">
                <Row>
                    <Col sm="12" md={{ size: 12, offset: 4 }}>
                        <img src={"https://www.androidbeat.com/wp-content/uploads/2014/05/new-google-logo-1024x398.png?ezimgfmt=rs:579x225/rscb8/ng:webp/ngcb8"} />
                    </Col>
                </Row>
                <Row>
                    <Col sm="12" md={{ size: 12, offset: 5 }}>
                        <Button>Accept</Button>
                        <Button>Reject</Button>
                    </Col>
                </Row>
            </div>
        </>
    );
}

export default ImageValidator;

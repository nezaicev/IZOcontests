import React, {Component} from 'react';
import {render} from "react-dom";
import Button from '@mui/material/Button';
import {Box, Container, Link, Switch, Typography} from "@mui/material";
import CustomGrid from "./dataGrid";
import {Paper} from "@material-ui/core";
import * as PropTypes from "prop-types";




class App extends Component {
  render() {
    return(
        <div>
            test
        </div>

    );
}

}

export default App;


const container = document.getElementById("app");
render(<App/>, container);
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
    <Container maxWidth="lg">
      <Paper sx={{ p: 2, margin: 'auto', maxWidth: 500, flexGrow: 1 }}>
      <CustomGrid/>
      </Paper>
    </Container>
    );
}

}

export default App;


const container = document.getElementById("app");
render(<App/>, container);
import * as React from 'react';
import {createTheme} from "@mui/material/styles";
import ThemeProvider from "@mui/material/styles/ThemeProvider";
import Button from "@material-ui/core/Button";

const theme = createTheme({
    components: {
        MuiButton: {
            styleOverrides: {
               button: {

                        fontSize: '1rem',
                        color:'#fff'


                },
            },
        },
    },
});

export default function GlobalTest (){
    return(
        <ThemeProvider theme={theme}>
            <Button >
                TEST
            </Button>
        </ThemeProvider>
    )
}
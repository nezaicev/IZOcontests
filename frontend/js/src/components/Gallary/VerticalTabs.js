import * as React from 'react';
import Box from '@mui/material/Box';
import Tabs, {tabsClasses} from '@mui/material/Tabs';
import Tab from '@mui/material/Tab';
import {createTheme} from "@mui/material";
import {ThemeProvider} from "@emotion/react";
import {customThemeTab} from "../styled";







export default function VerticalTabs(props) {
    const [value, setValue]= React.useState(0);

    const handleChange = (event, newValue) => {
        setValue(newValue);
        props.setValueVerticalTabs(newValue)
    };

    return (
        <Box
            sx={{
                // maxWidth: {xs: 320, sm: 480},
                width:'auto',
                height: 88,
                bgcolor: 'background.paper',
                display: 'flex',
            }}
        >
            <ThemeProvider theme={customThemeTab}>

            <Tabs
                value={value}
                onChange={handleChange}
                orientation="vertical"
                variant="scrollable"
                scrollButtons
                 allowScrollButtonsMobile
                textColor="inherit"
                aria-label="visible arrows tabs example"
                sx={{


                   [`& .${tabsClasses.indicator}`]:{

                          backgroundColor:'#d36666'
                    },
                    [`& .${tabsClasses.root}`]:{
                       '&.Mui-selected':{
                          color:'#d36666'}
                    },

                    [`& .${tabsClasses.scrollButtons}`]: {
                        '&.Mui-disabled': {
                            opacity: 1,
                            'background-color': '#efece3'
                        },
                        'height': 14,
                        'background-color': '#efece3',
                        opacity: 1,
                    },
                }}>

                {
                    props.data.map((item, index) => (
                        <Tab  label={item} value={index}
                             key={index}/>
                    ))
                }

            </Tabs>
</ThemeProvider>


        </Box>
    );
}

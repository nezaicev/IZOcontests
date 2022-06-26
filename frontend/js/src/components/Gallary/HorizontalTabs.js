import * as React from 'react';
import Box from '@mui/material/Box';
import Tabs, {tabsClasses} from '@mui/material/Tabs';
import Tab from '@mui/material/Tab';
import {useEffect} from "react";

export default function HorizontalTabs(props) {
    const [value, setValue] = React.useState(0);
    useEffect(() => {
        setValue(0)
    }, [props.valueVerticalTabs])

    const handleChange = (event, newValue) => {
        setValue(newValue);
        props.setValueHorizontalTabs(newValue)
    };

    return (
        <Box
            sx={{
                 // flexGrow: 1,
        maxWidth: { xs: 300, sm: 800, md:900 },
                bgcolor: 'background.paper',
            }}
        >
            <Tabs
                value={value}
                onChange={handleChange}
                variant="scrollable"
                scrollButtons
                allowScrollButtonsMobile
                textColor="inherit"
                aria-label="visible arrows tabs example"
                sx={{
                    height:48,
                    '&.MuiButtonBase-root-MuiTab-root.Mui-selected':{color:'#33a4a4'},
                   [`& .${tabsClasses.indicator}`]:{
                          backgroundColor:'#d36666'
                    },
                    [`& .${tabsClasses.scrollButtons}`]: {
                        '&.Mui-disabled': {opacity: 0.3},
                    },
                }}
            >

                {
                    props.data.map((item, index) => (
                        <Tab label={item} value={index}
                             key={index}/>
                    ))
                }
            </Tabs>
        </Box>
    );
}

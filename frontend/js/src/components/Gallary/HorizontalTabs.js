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
                maxWidth: {xs: 320, sm: 480},
                bgcolor: 'background.paper',
                display: 'flex',
            }}
        >
            <Tabs
                value={value}
                onChange={handleChange}
                variant="scrollable"
                scrollButtons
                aria-label="visible arrows tabs example"
                sx={{
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

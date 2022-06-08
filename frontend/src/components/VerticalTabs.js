import * as React from 'react';
import Box from '@mui/material/Box';
import Tabs, {tabsClasses} from '@mui/material/Tabs';
import Tab from '@mui/material/Tab';
import axios from "axios";
import {useEffect} from "react";



export default function VerticalTabs(props) {
    const [Items, setItems] = React.useState([]);
    const [value, setValue] = React.useState(0);

     function loadItems() {

        axios({
            method: "GET",
            url: props.url,
        })
            .then((res) => {

                setItems(() => {
                    return [...res.data];
                });
                setValue(res.data[0])

            })
            .catch((e) => {
                console.log(e);
            });

    }
     useEffect(() => {
        loadItems();

    }, []);


    const handleChange = (event, newValue) => {
        props.setYear(newValue)
        setValue(newValue);
        props.resetPage();
    };

    return (
        <Box
            sx={{
                maxWidth: {xs: 320, sm: 480},
                marginLeft: 5,
                height: 90,
                bgcolor: 'background.paper',
                display: 'flex',
            }}
        >
            <Tabs
                value={value}
                onChange={handleChange}
                textColor="inherit"
                orientation="vertical"
                variant="scrollable"
                scrollButtons
                aria-label="visible arrows tabs example"
                sx={{
                    [`& .${tabsClasses.indicator}`]:{
                          backgroundColor:'#d36666'
                    },
                    [`& .${tabsClasses.scrollButtons}`]: {
                        '&.Mui-disabled': {
                            opacity: 0.4,
                            'background-color': '#efece3'
                        },
                        'height': 20,
                        'background-color': '#efece3',
                    },
                }}
            >
                {
                    Items.map((item, index) => (
                        <Tab label={item} value={item}
                             key={index}/>
                    ))}
            </Tabs>
        </Box>
    );
}

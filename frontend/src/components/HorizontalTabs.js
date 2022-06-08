import Box from "@mui/material/Box";
import Tabs, {tabsClasses} from "@mui/material/Tabs"
import React, {useEffect} from "react";

import axios from "axios";
import {Tab} from "@mui/material";

export default function HorizontalTabs(props) {
    const [value, setValue] = React.useState('Все');
    const [Items, setItems] = React.useState(props.nominations);


    const handleChange = (event, newValue) => {
        props.setNomination(newValue)
        setValue(newValue);
        props.resetPage()
        props.resetLoadedData()
    };

    useEffect(() => {
        loadItems();
    }, []);


    useEffect(() => {
        props.loadData()
    }, [value])

    function loadItems() {

        axios({
            method: "GET",
            url: props.url,
        })
            .then((res) => {
                setItems(() => {
                    return [...res.data];
                });

            })
            .catch((e) => {
                console.log(e);
            });
    }

    return (
        <Box sx={{bgcolor: 'background.paper'}}>
            <Tabs
                sx={{
                    [`& .${tabsClasses.indicator}`]:{
                        backgroundColor:'#d36666',
                    }
                }}
                value={value}
                onChange={handleChange}
                variant="scrollable"
                scrollButtons="auto"
                textColor="inherit"
                aria-label="scrollable auto tabs example"
            ><Tab label={"Все"} value={'Все'} key={0}/>

                {
                    Items.map((item, index) => (
                        <Tab label={item.name} value={item.name}
                             key={index + 1}/>

                    ))}

            </Tabs>
        </Box>
    );
}
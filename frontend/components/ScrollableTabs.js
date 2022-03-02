import Box from "@material-ui/core/Box";
import Tabs from "@material-ui/core/Tabs";
import React from "react";
import Tab from "@material-ui/core/Tab";
import axios from "axios";

export default function ScrollableTabs(props) {
    const [value, setValue] = React.useState([]);

    const handleChange = (event, newValue) => {
        setValue(newValue);
    };

    function loadItems() {

        axios({
            method: "GET",
            url: "http://127.0.0.1:8000/frontend/api/archive",
            params: {contest_name: props.contest},
        })
            .then((res) => {
                setValue(() => {
                    return [...new Set([...res.data.results.map((b) => b)])];
                });

            })
            .catch((e) => {
                console.log(e);
            });
    }

    return (
        <Box sx={{ maxWidth: { xs: 320, sm: 480 }, bgcolor: 'background.paper' }}>
            <Tabs
                value={value}
                onChange={handleChange}
                variant="scrollable"
                scrollButtons="auto"
                aria-label="scrollable auto tabs example"
            >
                <Tab label="Item One" />
                <Tab label="Item Two" />
                <Tab label="Item Three" />
                <Tab label="Item Four" />
                <Tab label="Item Five" />
                <Tab label="Item Six" />
                <Tab label="Item Seven" />
            </Tabs>
        </Box>
    );
}
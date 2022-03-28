import Box from "@material-ui/core/Box";
import Tabs from "@material-ui/core/Tabs";
import React, {useEffect} from "react";
import Tab from "@material-ui/core/Tab";
import axios from "axios";

export default function ScrollableTabs(props) {
    const [value, setValue] = React.useState('Все');
    const [Items, setItems] = React.useState([]);

    const handleChange = (event, newValue) => {
        props.resetPage()
        props.setNomination(newValue)
        props.resetLoadedData()
        setValue(newValue);

    };

    useEffect(() => {
        loadItems();
    }, []);


    useEffect(()=>{
        props.loadData()


    },[value])

    function loadItems() {

        axios({
            method: "GET",
            url: props.url,
        })
            .then((res) => {
                setItems(() => {
                    return [...res.data.results];
                });

            })
            .catch((e) => {
                console.log(e);
            });
    }

    return (
        <Box sx={{ bgcolor: 'background.paper'}}>
            <Tabs
                value={value}
                onChange={handleChange}
                variant="scrollable"
                scrollButtons="auto"
                indicatorColor="secondary"
                aria-label="scrollable auto tabs example"
            ><Tab label={"Все"} value={'Все'} key={0}/>

                {
                    Items.map((item, index) => (
                    <Tab label={item.name} value={item.name} key={index+1}/>

                ))}

            </Tabs>
        </Box>
    );
}
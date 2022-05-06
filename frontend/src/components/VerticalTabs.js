import Box from "@material-ui/core/Box";
import Tabs from "@material-ui/core/Tabs";
import React, {useEffect} from "react";
import Tab from "@material-ui/core/Tab";
import axios from "axios";
import {tabsClasses} from "@mui/material";
import {styled} from '@mui/material/styles';

const StyledTabs=styled(Tabs)(()=>({
"& .MuiTabScrollButton-vertical":{height:20}

}))



export default function VerticalTabs(props) {
    const [value, setValue] = React.useState('Все');
    const [Items, setItems] = React.useState([]);



    const handleChange = (event, newValue) => {
        props.setNomination(newValue)
        setValue(newValue);
        props.resetPage()
        props.resetLoadedData()


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
        <Box sx={{  maxWidth: { xs: 320, sm: 480 },
                height:90,
                bgcolor: 'background.paper',
                display:'flex',}}>
            <StyledTabs
                value={value}
                orientation="vertical"
                onChange={handleChange}
                variant="scrollable"
                scrollButtons="auto"
                indicatorColor="secondary"

                // sx={{
                //     [`& .${tabsClasses.root}`]: {
                //         height: '20px',
                //     },
                // }}
            ><Tab label={"Все"} value={'Все'} key={0}/>

                {
                    Items.map((item, index) => (
                    <Tab label={item.name} value={item.name} key={index+1}/>

                ))}

            </StyledTabs>
        </Box>
    );
}
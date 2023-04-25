import AppBar from "@mui/material/AppBar";
import Container from "@mui/material/Container";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import React, {useEffect} from "react";
import IconButton from "@mui/material/IconButton";
import Box from "@mui/material/Box";
import Menu from "@mui/material/Menu";
import MenuItem from "@mui/material/MenuItem";
import MenuIcon from '@mui/icons-material/Menu';
import HomeIcon from "./HomeIcon";
import {useNavigate, useResolvedPath} from 'react-router-dom'
import Tab from "@mui/material/Tab";
import Tabs, {tabsClasses} from "@mui/material/Tabs";
import {Avatar} from "@mui/material";
import Tooltip from '@mui/material/Tooltip';
import {stringAvatar} from "../utils/utils";
import {AccountCircle} from "@mui/icons-material";

const host = process.env.REACT_APP_HOST_NAME


const Header = (props) => {

    // console.log(props.startPage, 'index_page')
    // console.log(typeof (props.startPage))
    // console.log(props.startPage === -1)
    const [tabs, setTabs] = React.useState(props.pages);
    const settings = [
        {name: 'Личный кабинет', link: `${host}/admin/`},
        props.auth.manager ? {name: 'Статистика', link: `${host}/frontend/page/statistics/`} : '',
        {name: 'Выход', link: `${host}/users/logout/?next_page=frontend/`}
    ]

    const initialSettings = [
        {name: 'Вход', link: `${host}/users/login/`},
        {name: 'Забыли пароль', link: `${host}/users/password_reset/`},
        {name: 'Регистрация', link: `${host}/users/signup/`},

    ]

    const [value, setValue] = React.useState(props.startPage === -1 ? 0 : props.startPage);


    useEffect(() => {
        setValue(props.startPage === -1 ? 0 : props.startPage)
    }, [props.pages])


    const handleChange = (event, newValue) => {
        setValue(newValue);
        navigate(props.pages[newValue]['link'])
        // console.log(newValue, 'click_tab')
    };


    const navigate = useNavigate()
    const [anchorElNav, setAnchorElNav] = React.useState(null);
    const [anchorElUser, setAnchorElUser] = React.useState(null);

    const handleOpenNavMenu = (event) => {
        setAnchorElNav(event.currentTarget);
    };
    const handleOpenUserMenu = (event) => {
        setAnchorElUser(event.currentTarget);
    };

    const handleCloseNavMenu = () => {
        setAnchorElNav(null);
    };

    const handleCloseUserMenu = () => {
        setAnchorElUser(null);
    };

    return (

        <AppBar position="static" sx={{bgcolor: '#816e6e'}}>
            <Container maxWidth="xl">
                <Toolbar disableGutters>

                    <Typography
                        variant="h6"
                        noWrap
                        component="div"
                        sx={{mr: 2, display: {xs: 'none', md: 'flex'}}}
                    >
                        <a href={props.mainLink ? props.mainLink : 'http://shkola-nemenskogo.ru/'}>
                            <HomeIcon sx={{fontSize: 60}}/>
                        </a>
                    </Typography>


                    <Box sx={{flexGrow: 1, display: {xs: 'flex', md: 'none'}}}>

                        <IconButton
                            size="large"
                            aria-label="account of current user"
                            aria-controls="menu-appbar"
                            aria-haspopup="true"
                            onClick={handleOpenNavMenu}
                            color="inherit"
                        >
                            <MenuIcon/>
                        </IconButton>

                        <Menu
                            id="menu-appbar"
                            anchorEl={anchorElNav}
                            anchorOrigin={{
                                vertical: 'bottom',
                                horizontal: 'left',
                            }}
                            keepMounted
                            transformOrigin={{
                                vertical: 'top',
                                horizontal: 'left',
                            }}
                            open={Boolean(anchorElNav)}
                            onClose={handleCloseNavMenu}
                            sx={{
                                display: {xs: 'block', md: 'none'},
                            }}
                        >
                            {props.pages ? props.pages.map((page, index) => (
                                <MenuItem key={index}
                                          onClick={() => {
                                              handleCloseNavMenu();
                                              props.activePage(index)
                                          }}>
                                    <Typography component='a'
                                                textAlign="center">{page['name']}</Typography>
                                </MenuItem>
                            )) : ''}
                        </Menu>
                    </Box>
                    <Typography
                        variant="h6"
                        noWrap
                        component="div"
                        sx={{flexGrow: 1, display: {xs: 'flex', md: 'none'}}}
                    >
                        <a href={props.mainLink ? props.mainLink : 'http://shkola-nemenskogo.ru/'}>
                            <HomeIcon sx={{fontSize: 45}}/>
                        </a>
                    </Typography>
                    <Box sx={{flexGrow: 1, display: {xs: 'none', md: 'flex'}}}>


                        <Tabs value={value} onChange={handleChange}
                              variant="scrollable"
                              scrollButtons="auto"
                              textColor="inherit"
                              sx={{

                                  [`& .${tabsClasses.indicator}`]: {
                                      backgroundColor: '#d36666'
                                  },
                                  [`& .${tabsClasses.scrollButtons}`]: {
                                      '&.Mui-disabled': {opacity: 0.3},
                                  },
                              }}
                        >
                            {props.pages ? props.pages.map((page, index) => (
                                <Tab key={index}
                                     label={page['name']}/>
                            )) : ''}
                        </Tabs>


                    </Box>
                    {props.auth['auth'] ? <Box sx={{flexGrow: 0}}>
                        <Tooltip title="Открыть меню">
                            <IconButton onClick={handleOpenUserMenu}
                                        sx={{p: 0}}>
                                <Avatar {...stringAvatar(props.auth['user'])} />
                            </IconButton>
                        </Tooltip>
                        <Menu
                            sx={{mt: '45px'}}
                            id="menu-appbar"
                            anchorEl={anchorElUser}
                            anchorOrigin={{
                                vertical: 'top',
                                horizontal: 'right',
                            }}
                            keepMounted
                            transformOrigin={{
                                vertical: 'top',
                                horizontal: 'right',
                            }}
                            open={Boolean(anchorElUser)}
                            onClose={handleCloseUserMenu}
                        >
                            {settings.map((setting, index) => (
                                <MenuItem key={index}
                                          onClick={() => {
                                              handleCloseUserMenu();
                                              window.location.replace(setting.link)
                                          }}>
                                    <Typography
                                        textAlign="center">{setting.name}</Typography>
                                </MenuItem>
                            ))}
                        </Menu>
                    </Box> : <div>
                        <IconButton

                            aria-label="account of current user"
                            aria-controls="menu-appbar"
                            aria-haspopup="true"
                            onClick={handleOpenUserMenu}
                            color="inherit"
                        >
                            <AccountCircle sx={{fontSize: 35}}/>
                        </IconButton>
                        <Menu
                            id="menu-appbar"
                            anchorEl={anchorElUser}
                            anchorOrigin={{
                                vertical: 'top',
                                horizontal: 'right',
                            }}
                            keepMounted
                            transformOrigin={{
                                vertical: 'top',
                                horizontal: 'right',
                            }}
                            open={Boolean(anchorElUser)}
                            onClose={handleCloseUserMenu}
                        >
                            {initialSettings.map((setting, index) => (
                                <MenuItem key={setting.name}
                                          onClick={() => {
                                              handleCloseUserMenu();
                                              window.location.replace(setting.link)
                                          }}>
                                    <Typography
                                        textAlign="center">{setting.name}</Typography>
                                </MenuItem>))
                            }


                        </Menu>
                    </div>}
                </Toolbar>
            </Container>

        </AppBar>
    );
};
export default Header;

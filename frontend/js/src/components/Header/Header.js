import AppBar from "@mui/material/AppBar";
import Container from "@mui/material/Container";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import React from "react";
import IconButton from "@mui/material/IconButton";
import Box from "@mui/material/Box";
import Menu from "@mui/material/Menu";
import MenuItem from "@mui/material/MenuItem";
import Button from "@mui/material/Button";
import MenuIcon from '@mui/icons-material/Menu';
import HomeIcon from "./HomeIcon";

const Header = (props) => {
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
                        <a href='http://shkola-nemenskogo.ru/'>
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
                            {props.pages.map((page) => (
                                <MenuItem key={page['name']}
                                          onClick={handleCloseNavMenu}>
                                    <Typography component='a'
                                        textAlign="center">{page['name']}</Typography>
                                </MenuItem>
                            ))}
                        </Menu>
                    </Box>
                    <Typography
                        variant="h6"
                        noWrap
                        component="div"
                        sx={{flexGrow: 1, display: {xs: 'flex', md: 'none'}}}
                    >
                        <HomeIcon sx={{fontSize: 45}}/>
                    </Typography>
                    <Box sx={{flexGrow: 1, display: {xs: 'none', md: 'flex'}}}>
                        {/*{pages.map((page) => (*/}
                        {/*    <Button*/}
                        {/*        key={page}*/}
                        {/*        onClick={handleCloseNavMenu}*/}
                        {/*        sx={{my: 2, color: 'white', display: 'block'}}*/}
                        {/*    >*/}
                        {/*        {page}*/}
                        {/*    </Button>*/}
                        {/*))}*/}
                    </Box>

                    {/*<Box sx={{ flexGrow: 0 }}>*/}
                    {/*  <Tooltip title="Open settings">*/}
                    {/*    <IconButton onClick={handleOpenUserMenu} sx={{ p: 0 }}>*/}
                    {/*      <Avatar alt="Remy Sharp" src="/static/images/avatar/2.jpg" />*/}
                    {/*    </IconButton>*/}
                    {/*  </Tooltip>*/}
                    {/*  <Menu*/}
                    {/*    sx={{ mt: '45px' }}*/}
                    {/*    id="menu-appbar"*/}
                    {/*    anchorEl={anchorElUser}*/}
                    {/*    anchorOrigin={{*/}
                    {/*      vertical: 'top',*/}
                    {/*      horizontal: 'right',*/}
                    {/*    }}*/}
                    {/*    keepMounted*/}
                    {/*    transformOrigin={{*/}
                    {/*      vertical: 'top',*/}
                    {/*      horizontal: 'right',*/}
                    {/*    }}*/}
                    {/*    open={Boolean(anchorElUser)}*/}
                    {/*    onClose={handleCloseUserMenu}*/}
                    {/*  >*/}
                    {/*    {settings.map((setting) => (*/}
                    {/*      <MenuItem key={setting} onClick={handleCloseUserMenu}>*/}
                    {/*        <Typography textAlign="center">{setting}</Typography>*/}
                    {/*      </MenuItem>*/}
                    {/*    ))}*/}
                    {/*  </Menu>*/}
                    {/*</Box>*/}
                </Toolbar>
            </Container>

        </AppBar>
    );
};
export default Header;

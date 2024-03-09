const fetch = require('node-fetch');
const open = require('open');

const username = '31dww2rwdzxhieztk7dj4adaerlm';
const clientID = '400277d6458a4792986c24617fc581dd';
const clientSecret = '84fb5cd442d94eaaab0b9ad6e314acb1';
const redirect_uri = 'http://127.0.0.1:8000/';

const getUserInfo = async (token) => {
    const response = await fetch('https://api.spotify.com/v1/me', {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${token}`
        }
    });
    return await response.json();
}

const searchAndOpenSong = async (spotifyObject) => {
    const search_song = prompt("Enter the song name: ");
    const response = await spotifyObject.search(search_song, { type: 'track', limit: 1 });
    const songUrl = response.tracks.items[0].external_urls.spotify;
    open(songUrl);
    console.log('Song has opened in your browser.');
}

const main = async () => {
    const tokenResponse = await fetch('https://accounts.spotify.com/api/token', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic ' + Buffer.from(clientID + ':' + clientSecret).toString('base64')
        },
        body: new URLSearchParams({
            'grant_type': 'client_credentials'
        })
    });
    const tokenData = await tokenResponse.json();
    const token = tokenData.access_token;

    const userInfo = await getUserInfo(token);
    console.log(userInfo.display_name ? `Welcome to the project, ${userInfo.display_name}` : "Welcome!");

    while (true) {
        console.log("0 - Exit the console");
        console.log("1 - Search for a Song");

        const user_input = parseInt(prompt("Enter Your Choice: "));
        if (user_input === 1) {
            await searchAndOpenSong(token);
        } else if (user_input === 0) {
            console.log("Good Bye, Have a great day!");
            break;
        } else {
            console.log("Please enter valid user-input.");
        }
    }
}

main();

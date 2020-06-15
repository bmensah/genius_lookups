
<h1> Genius Lookups </h1>

<p> A program that scrapes browser history, finds lyrics lookups on Genius.com, and puts the songs into a Spotify playlist. </p>

<p> Inspired by <a href='https://github.com/TheComeUpCode/SpotifyGeneratePlaylist'> TheComeUpCode - SpotifyGeneratePlaylist</a>. Many Thanks! </p>

<h3> Table of Contents </h3>
<ul> 
  <li id= "setup"> Set Up </li>
  <li id="modules"> Modules and APIs Used </li>
  <li id="issues"> Issues/ToDo </li>
  
</ul>

<h3 href=#setup>Set Up</h3>

<h5>Finding your spotify user ID:</h5>
<p> Your user ID is a 10 digit number that can be found easily via the Spotify Mobile app. Click on Settings -> Account and your user ID is listed right there next to "Username." </p>
<p> Your user ID can also be found via the Spotify Desktop app. Go to the Spotify app on your Desktop. Click on your name on the upper right hand corner. This will bring you to your User page. Find the three-dot menu button under where your username is written in big letters. Click on this, then click on Share -> Copy Spotify URI. Paste the URI into the secrets.py file and remove the "spotify:user:" tags. Leave only the number. </p>
<h5>Getting a Token:</h5>
<p> Click <a href="https://developer.spotify.com/console/post-playlists/"> here </a> to get an authentication token to create and add songs to a playlist. You will need to input your user ID, then press "Get Token". The only scopes you need for this project are 'playlist-modify-public' or 'playlist-modify-private.'</p>
<p>Note: The token expires in about 30 minutes or so. If you are having trouble creating the playlist, try generating a new token.</p>
<h5>Running the Project:</h5>
<p>Once you download the files and add your Spotify user ID and an OAuth tag to the 'secrets.py' file, simply run the 'add_songs' program.</p>

<h3 href=#modules>Modules and APIs Used</h3>
<ul>
  <li> Spotify API </li>
  <li> requests Library </li>
  <li> browserhistory </li>
  <li> BeautifulSoup </li>
  <li> unicodedata </li>
  <li> json </li>
  <li> unidecode </li>
</ul>



<h3 href=#issues>Issues/ToDo</h3> 
<ul>
<li> Program currently only works with Chrome broswer on a Mac, but I am working on updating the code to work on all systems and browsers. </li>
</ul>

<p> Please contact me if in using this module you run into any other issues. </p>


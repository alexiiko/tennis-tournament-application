import { orsURL, orsAuthToken, orsGEOCODEAuthToken } from "./serviceCredentials.js"

async function getTournamentAddressCoordinates(tournamentAdress) {
  const orsAPIGeocodeResponse = await fetch(`https://api.openrouteservice.org/geocode/search?api_key=${orsGEOCODEAuthToken}&text=${encodeURIComponent(tournamentAdress)}`)
  const data = await orsAPIGeocodeResponse.json()
  const tournamentCoordinates = data.features[0].geometry.coordinates
  return tournamentCoordinates
}

async function getUserAdressCoordinates(userAddress) {
  const orsAPIGeocodeResponse = await fetch(`https://api.openrouteservice.org/geocode/search?api_key=${orsGEOCODEAuthToken}&text=${encodeURIComponent(userAddress)}`)
  const data = await orsAPIGeocodeResponse.json()
  const userCoordinates = data.features[0].geometry.coordinates

  return userCoordinates
}

export async function retrieveDistanceAndTimeBetweenTournamentAndUser(userAddress, tournamentAddress) {
  const userAddressCoordinates = await getUserAdressCoordinates(userAddress)
  const tournamentAdressCoordinates = await getTournamentAddressCoordinates(tournamentAddress) 
  
  const orsAPIResponse = await fetch(orsURL, {
    method: 'POST',
    headers: {
      'Authorization': `${orsAuthToken}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      coordinates: [userAddressCoordinates, tournamentAdressCoordinates],
    }),
  })

  const data = await orsAPIResponse.json()
  const timeAndDurationObject = data.routes[0].summary

  const distanceToGetToTournament = Math.round(timeAndDurationObject.distance / 1000) // we divide by 1000 as the duration given by the api is in meters
  const timeToGetToTournament = Math.round(timeAndDurationObject.duration / 60) // we divide by 60 as the duration given by the api is in seconds 

  return [distanceToGetToTournament, timeToGetToTournament]
}

// we access the tournament data via https as turso does not support compatibility with react native  
import { dbAuthToken, dbURL } from "./dbCredentials.js"

export async function retrieveTournaments(ageClass) {
  const tursoAPIResponse = await fetch( dbURL,{
    method: "POST",
    headers: {
      "Authorization": `Bearer ${dbAuthToken}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      requests: [
        {
          type: "execute",
          stmt: {
            sql: `SELECT * FROM ${ageClass}`
          }
        },
      ],
    }),
  });
  const rawData = await tursoAPIResponse.json();
  const tournaments = rawData.results[0].response.result.rows
  return tournaments
}
// todo:
// - add error handling 

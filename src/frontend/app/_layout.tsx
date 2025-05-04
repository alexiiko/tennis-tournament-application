import {  Tabs } from "expo-router";

export default function RootLayout() {
  return <Tabs>
        <Tabs.Screen name="searchTournaments" options={{ title: "Turniere suchen"}}/>
        <Tabs.Screen name="savedTournaments" options={{ title: "gespeicherte Turniere"}}/>
        <Tabs.Screen name="settings" options={{ title: "Einstellungen"}}/>
    </Tabs>
}

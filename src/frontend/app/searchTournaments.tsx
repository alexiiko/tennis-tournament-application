import { Text } from "@react-navigation/elements";
import { retrieveDBData } from "../services/fetchDataDB.js";
import { View } from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";
import { Button } from "react-native-paper";

export default function main() {
    return (
      <SafeAreaView>
        <View>
          <View style={{ borderWidth: 1, borderColor: "grey", padding: 10, borderRadius: 7, marginLeft: 5, marginRight: 5, }}>
            <View style={{ justifyContent: "center" }}>
                <Button icon="filter" textColor="black" buttonColor="transparent" style={{ position: "absolute", left: 0}}> </Button>
                <Button icon="magnify" textColor="black" buttonColor="transparent" style={{ position: "absolute", right: 0}}> </Button>
            </View>
          </View>
        </View>
      </SafeAreaView>
    )
}

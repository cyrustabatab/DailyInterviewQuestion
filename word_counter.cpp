#include <fstream>
#include <vector>
#include <sstream>
#include <string>
#include <map>



std::vector<std::string> load_words_from_file(const std::string& file_name) {
    

    std::ifstream input_file{file_name};
    
    std::vector<std::string> words{};
    if(input_file) {
        
        std::string line{};
        std::stringstreams ss{}; 
        while(std::getline(input_file,line)) {
            
            ss.str(line);
            ss.clear();
            
            std::string word{};
            while(ss >> word) {
                words.push_back(word); 

            }
        }


    }

    return words;

}

int main() {

    const std::string file_name{"words.txt"};


    std::map<std::string,int> word_counts;


}

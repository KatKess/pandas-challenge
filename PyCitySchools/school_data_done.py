{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "8a3a252c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "6897e22b",
   "metadata": {},
   "outputs": [],
   "source": [
    "#File to Load\n",
    "school_data_to_load = \"Resources/schools_complete.csv\"\n",
    "student_data_to_load = \"Resources/students_complete.csv\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "6d5b5b90",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Read School and Student Data File and store into Pandas DataFrames\n",
    "school_data = pd.read_csv(school_data_to_load)\n",
    "student_data = pd.read_csv(student_data_to_load)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "fdf73857",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Student ID</th>\n",
       "      <th>student_name</th>\n",
       "      <th>gender</th>\n",
       "      <th>grade</th>\n",
       "      <th>school_name</th>\n",
       "      <th>reading_score</th>\n",
       "      <th>math_score</th>\n",
       "      <th>School ID</th>\n",
       "      <th>type</th>\n",
       "      <th>size</th>\n",
       "      <th>budget</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>Paul Bradley</td>\n",
       "      <td>M</td>\n",
       "      <td>9th</td>\n",
       "      <td>Huang High School</td>\n",
       "      <td>66</td>\n",
       "      <td>79</td>\n",
       "      <td>0</td>\n",
       "      <td>District</td>\n",
       "      <td>2917</td>\n",
       "      <td>1910635</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>Victor Smith</td>\n",
       "      <td>M</td>\n",
       "      <td>12th</td>\n",
       "      <td>Huang High School</td>\n",
       "      <td>94</td>\n",
       "      <td>61</td>\n",
       "      <td>0</td>\n",
       "      <td>District</td>\n",
       "      <td>2917</td>\n",
       "      <td>1910635</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>Kevin Rodriguez</td>\n",
       "      <td>M</td>\n",
       "      <td>12th</td>\n",
       "      <td>Huang High School</td>\n",
       "      <td>90</td>\n",
       "      <td>60</td>\n",
       "      <td>0</td>\n",
       "      <td>District</td>\n",
       "      <td>2917</td>\n",
       "      <td>1910635</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>Dr. Richard Scott</td>\n",
       "      <td>M</td>\n",
       "      <td>12th</td>\n",
       "      <td>Huang High School</td>\n",
       "      <td>67</td>\n",
       "      <td>58</td>\n",
       "      <td>0</td>\n",
       "      <td>District</td>\n",
       "      <td>2917</td>\n",
       "      <td>1910635</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>Bonnie Ray</td>\n",
       "      <td>F</td>\n",
       "      <td>9th</td>\n",
       "      <td>Huang High School</td>\n",
       "      <td>97</td>\n",
       "      <td>84</td>\n",
       "      <td>0</td>\n",
       "      <td>District</td>\n",
       "      <td>2917</td>\n",
       "      <td>1910635</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Student ID       student_name gender grade        school_name  \\\n",
       "0           0       Paul Bradley      M   9th  Huang High School   \n",
       "1           1       Victor Smith      M  12th  Huang High School   \n",
       "2           2    Kevin Rodriguez      M  12th  Huang High School   \n",
       "3           3  Dr. Richard Scott      M  12th  Huang High School   \n",
       "4           4         Bonnie Ray      F   9th  Huang High School   \n",
       "\n",
       "   reading_score  math_score  School ID      type  size   budget  \n",
       "0             66          79          0  District  2917  1910635  \n",
       "1             94          61          0  District  2917  1910635  \n",
       "2             90          60          0  District  2917  1910635  \n",
       "3             67          58          0  District  2917  1910635  \n",
       "4             97          84          0  District  2917  1910635  "
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Combine the data into a single dataset.\n",
    "school_data_complete = pd.merge(student_data, school_data, how=\"left\", on=[\"school_name\", \"school_name\"])\n",
    "school_data_complete.head()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "c228859c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "15\n"
     ]
    }
   ],
   "source": [
    "#Calculate the total number of unique schools\n",
    "school_count_df = pd.DataFrame(school_data_complete)\n",
    "print(school_count_df['school_name'].nunique())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "0900318a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "39170"
      ]
     },
     "execution_count": 79,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Calculate the total number of students.\n",
    "student_count_df = pd.DataFrame(school_data_complete)\n",
    "student_count_df.student_name.count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "79197f32",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "24649428\n"
     ]
    }
   ],
   "source": [
    "#Calculate the total budget\n",
    "total_budget_df = pd.DataFrame(school_data)\n",
    "print(total_budget_df['budget'].sum())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "84b154a3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "78.98537145774827"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Calculate the average (mean)math score\n",
    "average_math_score_df = pd.DataFrame(school_data_complete)\n",
    "average_math_score_df.math_score.mean()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "7289194a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "81.87784018381414"
      ]
     },
     "execution_count": 87,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Calculate the average (mean) reading score\n",
    "average_reading_score_df = pd.DataFrame(school_data_complete)\n",
    "average_reading_score_df.reading_score.mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "0875196a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "74.9808526933878"
      ]
     },
     "execution_count": 93,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Get the student count of those who passed math.\n",
    "student_cnt = '39170'\n",
    "\n",
    "# Calculate the percentage of students who passed math (math scores greather than or equal to 70)\n",
    "passing_math_cnt = school_data_complete[(school_data_complete[\"math_score\"] >= 70)].count()[\"student_name\"]\n",
    "passing_math_percentage = passing_math_cnt / float(student_cnt) * 100\n",
    "passing_math_percentage"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "id": "4974454d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "85.80546336482001"
      ]
     },
     "execution_count": 94,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Calculate the percentage of students who passeed reading\n",
    "passing_reading_cnt = school_data_complete[(school_data_complete[\"reading_score\"] >= 70)].count()[\"student_name\"]\n",
    "passing_reading_percentage = passing_reading_cnt / float(student_cnt) * 100\n",
    "passing_reading_percentage\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "id": "9a9c0d09",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "65.17232575950983"
      ]
     },
     "execution_count": 96,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use the following to calculate the percentage of students that passed math and reading\n",
    "passing_math_reading_count = school_data_complete[\n",
    "    (school_data_complete[\"math_score\"] >= 70) & (school_data_complete[\"reading_score\"] >= 70)\n",
    "].count()[\"student_name\"]\n",
    "overall_passing_rate = passing_math_reading_count /  float(student_cnt) * 100\n",
    "overall_passing_rate"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "id": "d7ffc777",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Total Schools</th>\n",
       "      <th>Total Students</th>\n",
       "      <th>Total Budget</th>\n",
       "      <th>Average Math Score</th>\n",
       "      <th>Average Reading Score</th>\n",
       "      <th>% Passing Math</th>\n",
       "      <th>% Passing Reading</th>\n",
       "      <th>% Overall Passing</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>15</td>\n",
       "      <td>39,170</td>\n",
       "      <td>$24,649,428.00</td>\n",
       "      <td>78.99</td>\n",
       "      <td>81.88</td>\n",
       "      <td>74.98</td>\n",
       "      <td>85.81</td>\n",
       "      <td>65.17</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Total Schools Total Students    Total Budget Average Math Score  \\\n",
       "0            15         39,170  $24,649,428.00              78.99   \n",
       "\n",
       "  Average Reading Score % Passing Math % Passing Reading % Overall Passing  \n",
       "0                 81.88          74.98             85.81             65.17  "
      ]
     },
     "execution_count": 122,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Create a high-level snapshot of the district's key metrics in a DataFrame\n",
    "district_summary_df = pd.DataFrame({\"Total Schools\":[15],\n",
    "                                   \"Total Students\":[39170],\n",
    "                                   \"Total Budget\":[24649428],\n",
    "                                   \"Average Math Score\":[78.98537145774827],\n",
    "                                   \"Average Reading Score\":[81.87784018381414],\n",
    "                                   \"% Passing Math\":[74.9808526933878],\n",
    "                                   \"% Passing Reading\":[85.80546336482001],\n",
    "                                   \"% Overall Passing\":[65.17232575950983],})\n",
    "\n",
    "district_summary = district_summary_df\n",
    "# Formatting\n",
    "district_summary[\"Total Schools\"]= district_summary[\"Total Schools\"].map(\"{:,}\".format)\n",
    "district_summary[\"Total Students\"] = district_summary[\"Total Students\"].map(\"{:,}\".format)\n",
    "district_summary[\"Total Budget\"] = district_summary[\"Total Budget\"].map(\"${:,.2f}\".format)\n",
    "district_summary[\"Average Math Score\"]=district_summary[\"Average Math Score\"].map(\"{:,.2f}\".format)\n",
    "district_summary[\"Average Reading Score\"]=district_summary[\"Average Reading Score\"].map(\"{:,.2f}\".format)\n",
    "district_summary[\"% Passing Math\"]=district_summary[\"% Passing Math\"].map(\"{:,.2f}\".format)\n",
    "district_summary[\"% Passing Reading\"]=district_summary[\"% Passing Reading\"].map(\"{:,.2f}\".format)\n",
    "district_summary[\"% Overall Passing\"]=district_summary[\"% Overall Passing\"].map(\"{:,.2f}\".format)\n",
    "# Display the DataFrame\n",
    "district_summary"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c2764d9b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

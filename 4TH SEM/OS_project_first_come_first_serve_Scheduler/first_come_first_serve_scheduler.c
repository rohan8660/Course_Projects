#include <stdio.h>
#include <stdlib.h>
int total_no_process;
int process_limit = 19;

int main()
{
    int i;
    printf("\n");
    printf("********************************************************************************\n");
    printf("TIME CALCULATOR FOR FIRST COME FIRST SERVE (FCFS) SCHEDULER \n");
    printf("********************************************************************************\n");
    printf("\n");
    printf("Enter The Total Number Of Processes : \n");
    scanf("%d", &total_no_process);
    while (total_no_process > process_limit)
    {
        printf("Please Enter Number Of Processes Less Than %d :)\n", (process_limit + 1));
        printf("Enter The Total Number Of Processes : \n");
        scanf("%d", &total_no_process);
    }
    float burst_time[total_no_process];
    float arrival_time[total_no_process];
    float turnaround_time[total_no_process];
    float waiting_time[total_no_process];
    float avg_turnaround_time;
    float avg_waiting_time;

    for (i = 1; i < (total_no_process + 1); i++)
    {
        printf("enter the burst time for Process %d >>", i);
        scanf("%f", &burst_time[i]);

        printf("enter the arrival time for Process %d >>", i);
        scanf("%f", &arrival_time[i]);

        printf("\n");
    }
    //sorting
    arrival_time[0] = 0;
    burst_time[0] = 0;
    int j;
    float temp, temp1;
    for (i = 1; i < (total_no_process + 1); i++)
        for (j = 1; j < (total_no_process - i + 1); j++)
            if (arrival_time[j] > arrival_time[j + 1])
            {
                temp = arrival_time[j];
                arrival_time[j] = arrival_time[j + 1];
                arrival_time[j + 1] = temp;

                temp1 = burst_time[j];
                burst_time[j] = burst_time[j + 1];
                burst_time[j + 1] = temp1;
            }

    //this is calculating waiting time
    float sum_burst_time = 0;
    for (i = 1; i < (total_no_process + 1); i++)
    {
        if (i == 1)
        {
            waiting_time[i] = arrival_time[i];
        }
        else
        {
            waiting_time[i] = sum_burst_time - arrival_time[i];
        }
        sum_burst_time = sum_burst_time + burst_time[i];
    }
    // this is for calculating turnaround time
    for (i = 1; i < (total_no_process + 1); i++)
    {
        turnaround_time[i] = waiting_time[i] + burst_time[i];
    }
    //avg waiting time
    for (i = 1; i < (total_no_process + 1); i++)
    {
        avg_waiting_time = avg_waiting_time + waiting_time[i];
    }
    avg_waiting_time = avg_waiting_time / total_no_process;
    //avg waiting time
    for (i = 1; i < (total_no_process + 1); i++)
    {
        avg_turnaround_time = avg_turnaround_time + turnaround_time[i];
    }
    avg_turnaround_time = avg_turnaround_time / total_no_process;

    printf("\n");
    printf("---------------------------------------------------------------------------------\n");
    printf("Process No \t Arrival Time \t Burst Time \t Waiting Time \t Turnaround Time \n");
    printf("---------------------------------------------------------------------------------\n");
    for (int j = 1; j < (total_no_process + 1); j++)
    {
        printf("        %d\t  %0.3f\t   %0.3f\t    %0.3f\t   %0.3f\n\n", j, arrival_time[j], burst_time[j], waiting_time[j], turnaround_time[j]);
    }
    printf("---------------------------------------------------------------------------------\n");
    printf("Average Waiting Time is %0.3f \n\n", avg_waiting_time);
    printf("Average Turnaround Time is %0.3f \n", avg_turnaround_time);
    printf("---------------------------------------------------------------------------------\n");
}
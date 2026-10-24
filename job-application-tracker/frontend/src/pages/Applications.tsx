import { useState, useEffect } from "react";

import { getApplications } from "../api/application";
import type { FormEvent } from "react";

import {
    JobApplicationListResponse,
    ApplicationFilters
} from "../types/application";


const [company_name,setCompanyname] = useState("");
const [job_title,setJobtitle] = useState("");
const [resume_used,setResumeused] = useState("");
const [status,setStatus] = useStatus("")

const [items,setItems] = useState<JobApplicationListResponse[]>[];
const [error,setError] = useState("");
const [loading,setLoading] = useState(false);
const [pages,setPages] = useState(1);
const [total,setTotal] = useState(1);
const [total_pages,setTotalPages] = useState(1);


async function load_applications{

    setLoading(true);

    try{

       const response = await getApplications({
        company_name: company_name,
        job_title: job_title,
        status: status,
        resume_used: resume_used,
        page: page,
        page_size: page_size
      }
    );

      setItems(response.items);
      setTotalpages(response.total_pages);
      setTotal(response.total);
    }catch(error){
        if (error instanceof Error){
            setError(error.message);
        }
        else{
            setError("Couldn't fetch applications");
        }
    }finally{
        setLoading(false);
    }

}

useEffect(()=>{
    load_applications;
},[pages]);


const handlesearch =(event:FormEvent<HTMLFormElement>)=>{
 load_applications();

};


const handleclear=()=>{
    setCompanyname("");
    setJobtitle("");
    setStatus("");
    setResumeused("");
};


return(
    <div>
        <div>
            <label>Search by compnay name</label>
            <Input
             value={company_name}
             type="text"
             onChange={(event)=>setCompanyname(event.target.value)}>

            <label>Search by job title</label>
            <Input
             value={job_title}
             type="text"
             onChange={(event)=>setJobtitle(event.target.value)}/>
        </div>

        <div>
            <button
             onClick={handleSearch}>Search</button>
        </div>

        <div>
            <button 
             onClick={handleclear}>Clear filters</button>
        </div>

        <select
        <option
        value={resume_send}
        onClick={(event)=>setResumeused(event.target.value)}></option>

        <table>
           <thead>
            <tr>Company Name</tr>
            <tr>Job title</tr>
            <tr></tr>
           </thead>
           {items.map{(item)key=item.id}}
           <tr>
            <td>
                item.company_name
            </td>
            <td>
                item.job_title
            </td>
            <td>
                item.source
            </td>
           </tr>
            
            </table>

            <div>
                <button
                 disable={total_pages==1}
                 onClick={setTotalPages(total_pages - 1)}>
                    Previous
                 </button>

            </div>

            <div>
                <button
                disable={total_pages}
                onClick={setPages(current)=>current + 1}>
                    Next

                </button>

                {error && <span>
                    No applications fetched</span>}

                <p>Returned {total} application{total===1? "s":""}</p>
            </div>

    </div>
);

export defualt
